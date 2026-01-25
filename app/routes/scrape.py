from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.database import get_db
from app.models.job import ScrapingJob
from app.models.product import Product
from app.services.scraper import CodeCanyonScraper
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uuid

router = APIRouter(prefix="/api/scrape", tags=["Scraping"])
templates = Jinja2Templates(directory="templates")

@router.post("", response_class=HTMLResponse)
async def init_scrape(
    request: Request,
    url: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # Basic URL validation
    if not any(k in url for k in ["codecanyon.net/item/", "codecanyon.net/search", "codecanyon.net/category/"]):
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

    # Create new job
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
        "progress": 0
    })

@router.get("/status/{job_id}", response_class=HTMLResponse)
async def get_job_status(
    job_id: str,
    request: Request,
    db: AsyncSession = Depends(get_db)
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
        product_query = select(Product).where(Product.id == job.result_product_id)
        product_result = await db.execute(product_query)
        product = product_result.scalars().first()
        return templates.TemplateResponse("components/product_card.html", {
            "request": request,
            "product": product
        })

    if job.status == "failed":
        return HTMLResponse(f"<div class='p-4 bg-red-100 text-red-700 rounded-lg'>Scraping failed: {job.error_message}</div>")

    # If pending or processing, we "process" it here for Vercel simulator
    # Phase 3: Update - Just poll
    if job.status == "pending" or job.status == "processing":
         return templates.TemplateResponse("components/scraping_progress.html", {
            "request": request,
            "job_id": job_id,
            "status": job.status,
            "progress": 20 if job.status == "pending" else 60
        })

    # This catch-all return might strictly not be needed if all statuses covered
    return HTMLResponse(f"<div class='p-4 bg-red-100 text-red-700 rounded-lg'>Unknown status: {job.status}</div>")

    # Still processing (shouldn't really happen with current simplified logic, but for polling completeness)
    return templates.TemplateResponse("components/scraping_progress.html", {
        "request": request,
        "job_id": job_id,
        "status": job.status,
        "progress": 50
    })
