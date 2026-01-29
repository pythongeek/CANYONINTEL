from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
import uuid
from app.database import get_db
from app.models.product import Product
from app.models.job import ScrapingJob
from app.utils.templates import templates

from app.models.analysis import AnalysisResult, UserProject

router = APIRouter(tags=["Dashboard"])

from app.utils.auth import login_required
from app.models.user import User

@router.get("/", response_class=HTMLResponse)
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: AsyncSession = Depends(get_db), current_user: User = Depends(login_required)):
    # Fetch stats
    try:
        total_products = await db.scalar(select(func.count(Product.id)))
        avg_profitability = await db.scalar(select(func.avg(Product.profitability_score))) or 0
        revenue_potential = await db.scalar(select(func.sum(Product.revenue_potential))) or 0
        active_projects = await db.scalar(select(func.count(UserProject.id)).where(UserProject.status != "launched")) or 0
    except Exception as e:
        print(f"Stats Error: {e}")
        total_products = 0
        avg_profitability = 0
        revenue_potential = 0
        active_projects = 0

    stats = {
        "total_products": total_products,
        "avg_profitability": round(float(avg_profitability), 1),
        "revenue_potential": float(revenue_potential or 0),
        "active_projects": active_projects
    }

    # Recent Activity (Combined Scraping Jobs and Analysis Results)
    recent_activity = []
    try:
        # Fetch 5 most recent scraping jobs
        jobs_result = await db.execute(
            select(ScrapingJob).order_by(desc(ScrapingJob.created_at)).limit(5)
        )
        for job in jobs_result.scalars().all():
            recent_activity.append({
                "type": "Scrape",
                "content": f"Scrape {job.status}: {job.url[:30]}...",
                "time": job.created_at
            })

        # Fetch 5 most recent analysis results
        analysis_result = await db.execute(
            select(AnalysisResult).order_by(desc(AnalysisResult.created_at)).limit(5)
        )
        for result in analysis_result.scalars().all():
            recent_activity.append({
                "type": "Analysis",
                "content": f"Analysis generated for product ID {str(result.product_id)[:8]}",
                "time": result.created_at
            })
        
        # Sort and limit combined activity
        recent_activity.sort(key=lambda x: x["time"], reverse=True)
        recent_activity = recent_activity[:5]
    except Exception as e:
        print(f"Activity Error: {e}")

    # Fetch recent products
    result = await db.execute(
        select(Product)
        .order_by(desc(Product.created_at))
        .limit(10)
    )
    recent_products = result.scalars().all()

    context = {
        "request": request,
        "stats": stats,
        "recent_products": recent_products,
        "recent_activity": recent_activity
    }

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("pages/dashboard.html", context) # Or a fragment if needed

    return templates.TemplateResponse("pages/dashboard.html", context)

@router.get("/products", response_class=HTMLResponse)
async def products_library(
    request: Request, 
    sort: str = "date", 
    min_score: int = 0,
    category: str = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(login_required)
):
    query = select(Product)
    
    # Apply filters
    if min_score > 0:
        query = query.where(Product.profitability_score >= min_score)
    
    if category and category != "":
        query = query.where(Product.category == category)
    
    if sort == "sales":
        query = query.order_by(desc(Product.total_sales))
    elif sort == "score":
        query = query.order_by(desc(Product.profitability_score))
    elif sort == "price":
        query = query.order_by(desc(Product.price))
    else: # date
        query = query.order_by(desc(Product.created_at))
        
    result = await db.execute(query)
    products = result.scalars().all()
    
    # If HTMX request, return only the table body or a partial
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("components/product_table_body.html", {
            "request": request,
            "products": products
        })
    
    return templates.TemplateResponse("pages/products.html", {
        "request": request,
        "products": products,
        "current_sort": sort
    })

@router.get("/api/discovery-stats", response_class=HTMLResponse)
async def get_discovery_stats(request: Request, db: AsyncSession = Depends(get_db)):
    found_jobs = await db.scalar(select(func.count(ScrapingJob.id)).where(ScrapingJob.status != "failed"))
    completed_jobs = await db.scalar(select(func.count(ScrapingJob.id)).where(ScrapingJob.status == "completed"))
    
    discovery_stats = None
    if found_jobs > 0:
        discovery_stats = {
            "found": found_jobs,
            "scraped": completed_jobs
        }
    
    return templates.TemplateResponse("components/discovery_progress.html", {
        "request": request,
        "discovery_stats": discovery_stats
    })
@router.get("/product/{product_id}", response_class=HTMLResponse)
async def product_detail(product_id: str, request: Request, db: AsyncSession = Depends(get_db), current_user: User = Depends(login_required)):
    try:
        product_uuid = uuid.UUID(product_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Product ID")
    
    product = await db.get(Product, product_uuid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    stmt = select(AnalysisResult).where(AnalysisResult.product_id == product_uuid).order_by(AnalysisResult.created_at.desc())
    res = await db.execute(stmt)
    analysis = res.scalars().first()
    
    context = {
        "request": request,
        "product": product,
        "analysis": analysis
    }
    
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("pages/product_detail.html", context)
        
    return templates.TemplateResponse("pages/product_detail.html", context)
