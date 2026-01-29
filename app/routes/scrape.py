from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.database import get_db
from app.models.job import ScrapingJob
from app.models.product import Product
# from app.services.scraper import CodeCanyonScraper
from app.utils.templates import templates
from app.utils.auth import login_required
from app.models.user import User
from datetime import datetime
import uuid

router = APIRouter(prefix="/api/scrape", tags=["Scraping"])

@router.post("", response_class=HTMLResponse)
async def init_scrape(
    request: Request,
    url: str = Form(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(login_required)
):
    # Basic URL validation
    valid_keywords = ["codecanyon.net/item/", "codecanyon.net/search", "codecanyon.net/category/", "codecanyon.net/popular_item/"]
    if not any(k in url for k in valid_keywords):
        raise HTTPException(status_code=400, detail="Invalid CodeCanyon URL")

    # Check if job already exists for this URL in last 24h
    existing_job_query = select(ScrapingJob).where(
        ScrapingJob.url == url,
        ScrapingJob.status == "completed",
        ScrapingJob.created_at > (datetime.now().date())
    ).order_by(ScrapingJob.created_at.desc())
    
    result = await db.execute(existing_job_query)
    existing_job = result.scalars().first()
    
    if existing_job and existing_job.result_product_id:
        # Return the product card immediately if we have it
        product_query = select(Product).where(Product.id == existing_job.result_product_id)
        product_result = await db.execute(product_query)
        product = product_result.scalars().first()
        if product:
            return templates.TemplateResponse("components/product_card.html", {
                "request": request,
                "product": product
            })

    # Create new job - This will be picked up by the Local Worker
    job_id = uuid.uuid4()
    new_job = ScrapingJob(
        id=job_id,
        url=url,
        status="pending"
    )
    db.add(new_job)
    await db.commit()

    return templates.TemplateResponse("components/scraping_progress.html", {
        "request": request,
        "job_id": str(job_id),
        "status": "pending",
        "progress": 5
    })

@router.get("/status/{job_id}", response_class=HTMLResponse)
async def get_job_status(
    job_id: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(login_required)
):
    try:
        job_uuid = uuid.UUID(job_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Job ID")

    query = select(ScrapingJob).where(ScrapingJob.id == job_uuid)
    result = await db.execute(query)
    job = result.scalars().first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.status == "completed":
        # Check if it was a Discovery Job (no single product result)
        if not job.result_product_id:
             return HTMLResponse(
                """
                <div class='p-8 bg-blue-50 dark:bg-blue-900/20 text-blue-800 dark:text-blue-300 rounded-2xl border border-blue-200 dark:border-blue-800 animate-in fade-in zoom-in duration-500'>
                    <div class="flex items-center gap-6 mb-6">
                        <div class="size-16 rounded-full bg-blue-600 flex items-center justify-center text-white shadow-lg shadow-blue-500/20">
                            <span class="material-symbols-outlined text-4xl">travel_explore</span>
                        </div>
                        <div>
                            <h3 class="font-extrabold text-2xl">Discovery Pulse Complete!</h3>
                            <p class="text-sm opacity-90 font-medium">Multiple high-potential items have been indexed and queued for deep analysis.</p>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-3">
                        <a href="/" class="px-6 py-3 bg-blue-600 text-white font-bold rounded-xl hover:bg-blue-700 transition-all shadow-md text-sm flex items-center gap-2">
                            <span class="material-symbols-outlined text-sm">dashboard</span>
                            Go to Dashboard
                        </a>
                        <a href="/products" class="px-6 py-3 bg-white dark:bg-gray-800 text-blue-600 dark:text-blue-400 border border-blue-200 dark:border-blue-800 font-bold rounded-xl hover:bg-blue-50 dark:hover:bg-gray-700 transition-all text-sm flex items-center gap-2">
                            <span class="material-symbols-outlined text-sm">analytics</span>
                            Explore Library
                        </a>
                    </div>
                </div>
                """
            )
            
        product_query = select(Product).where(Product.id == job.result_product_id)
        product_result = await db.execute(product_query)
        product = product_result.scalars().first()
        
        # Returns a Success fragment with a link to the Planner
        return HTMLResponse(
            f"""
            <div class='p-8 bg-emerald-50 dark:bg-emerald-900/20 text-emerald-800 dark:text-emerald-300 rounded-3xl border border-emerald-200 dark:border-emerald-800 animate-in fade-in zoom-in duration-700 shadow-xl'>
                <div class="flex items-center gap-6 mb-8">
                    <div class="size-20 rounded-full bg-emerald-500 flex items-center justify-center text-white shadow-xl shadow-emerald-500/20 relative">
                         <span class="material-symbols-outlined text-5xl">check_circle</span>
                         <div class="absolute -top-1 -right-1 size-6 bg-white dark:bg-gray-900 rounded-full flex items-center justify-center border-2 border-emerald-500">
                             <div class="size-3 bg-emerald-500 rounded-full animate-ping"></div>
                         </div>
                    </div>
                    <div>
                        <h3 class="font-black text-3xl tracking-tight">Intel Harvested!</h3>
                        <p class="text-lg opacity-90 font-semibold">{product.title if product else 'Product'} data and AI analysis are ready.</p>
                    </div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <a href="/planner/{job.result_product_id}" 
                       class="group bg-primary hover:bg-blue-700 text-white font-black py-5 px-8 rounded-2xl transition-all shadow-2xl shadow-primary/30 flex items-center justify-center gap-3 text-lg">
                        <span class="material-symbols-outlined text-3xl group-hover:rotate-12 transition-transform">rocket_launch</span>
                        Generate Launch Roadmap
                    </a>
                    <div class="flex gap-2">
                        <button onclick="window.location.reload()" 
                                class="flex-1 bg-white dark:bg-gray-800 text-slate-700 dark:text-slate-300 border border-gray-200 dark:border-gray-700 font-bold py-5 px-4 rounded-2xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-all flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined">refresh</span>
                            New Scrape
                        </button>
                    </div>
                </div>
            </div>
            """
        )
        response.headers["HX-Trigger"] = '{"showMessage": {"message": "Intel Successfully Harvested!", "level": "success"}}'
        return response

    if job.status == "failed":
        response = HTMLResponse(f"<div class='p-4 bg-red-100 text-red-700 rounded-lg'>Scraping failed: {job.error_message}</div>")
        response.headers["HX-Trigger"] = '{"showMessage": {"message": "Scraping Failed. Please check the URL.", "level": "danger"}}'
        return response

    # While pending or processing, show progress
    progress = 10 if job.status == "pending" else 50
    return templates.TemplateResponse("components/scraping_progress.html", {
        "request": request,
        "job_id": job_id,
        "status": job.status,
        "progress": progress
    })
