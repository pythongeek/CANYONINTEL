import asyncio
import os
import logging
import json
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update
from datetime import datetime, timedelta

# Import models - Assuming app/models is accessible
# We need to ensure PYTHONPATH includes root
import sys
sys.path.append(os.getcwd())

from app.models.job import ScrapingJob
from app.models.product import Product
from app.models.analysis import AnalysisResult
from worker.scraper import PlaywrightScraper
from worker.analyzer import MarketAnalyzer

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CanyonWorker")

# Database Setup
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found")

# Fix for SQLAlchemy asyncpg: must start with postgresql+asyncpg://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Remove sslmode as it's not supported by asyncpg in the DSN
if "?sslmode=" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.split("?sslmode=")[0]
elif "&sslmode=" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.split("&sslmode=")[0]

from app.database import AsyncSessionLocal

async def process_job(job: ScrapingJob, session: AsyncSession):
    """Executes the full pipeline for a single job."""
    logger.info(f"Processing Job {job.id} - {job.url}")
    
    try:
        # 1. Update Status -> Processing
        job.status = "processing"
        await session.commit()

        # 2. Scrape (Playwright)
        scraper = PlaywrightScraper(headless=True)
        raw_data = await scraper.scrape_with_stealth(job.url)
        
        # 2.5 Handle Discovery Mode (Bulk Task Spawning)
        if isinstance(raw_data, list):
            urls = raw_data
            logger.info(f"Discovery Mode: Found {len(urls)} products. Spawning new jobs...")
            
            spawned_count = 0
            seven_days_ago = datetime.now() - timedelta(days=7)
            
            for url in urls:
                # 1. Check if ANY successful job for this URL was completed in the last 7 days
                time_stmt = select(ScrapingJob).where(
                    ScrapingJob.url == url, 
                    ScrapingJob.status == "completed",
                    ScrapingJob.completed_at >= seven_days_ago
                )
                time_res = await session.execute(time_stmt)
                if time_res.scalars().first():
                    # logger.info(f"Skipping {url} (scraped in last 7 days)")
                    continue

                # 2. Check if there's already a PENDING job for this URL to avoid queuing it twice
                pending_stmt = select(ScrapingJob).where(
                    ScrapingJob.url == url, 
                    ScrapingJob.status == "pending"
                )
                pending_res = await session.execute(pending_stmt)
                if pending_res.scalars().first():
                    continue

                # 3. Queue new job
                new_job = ScrapingJob(
                    url=url,
                    status="pending"
                )
                session.add(new_job)
                spawned_count += 1
            
            job.status = "completed"
            job.completed_at = datetime.now()
            job.error_message = f"Discovered {len(urls)} items. Spawned {spawned_count} new tasks."
            await session.commit()
            logger.info(f"Discovery Job {job.id} Completed. {spawned_count} sub-jobs spawned.")
            return

        logger.info(f"Scraped Data: {raw_data.get('title', 'N/A')}")

        # 3. Analyze (Gemini)
        logger.info(f"Calling Gemini AI for [{raw_data.get('title', 'Unknown')}]...")
        analyzer = MarketAnalyzer()
        analysis = await analyzer.analyze_product(raw_data)
        
        # 3.5 Generate Blueprint (Gap Analysis)
        logger.info(f"Generating AI Blueprint for [{raw_data.get('title', 'Unknown')}]...")
        comments = raw_data.get("comments", [])
        blueprint = await analyzer.generate_blueprint(raw_data, comments)
        
        # Merge basic metrics back to product raw data
        raw_data["profitability_score"] = analysis.get("profitability_score", 0)
        raw_data["market_saturation"] = analysis.get("market_saturation", 0)
        raw_data["scraped_at"] = datetime.now()

        # 4. Save Product
        product_columns = {c.name for c in Product.__table__.columns}
        filtered_data = {k: v for k, v in raw_data.items() if k in product_columns}
        
        prod_stmt = select(Product).where(Product.codecanyon_id == str(raw_data.get('codecanyon_id', '')))
        res = await session.execute(prod_stmt)
        existing_product = res.scalars().first()
        
        if existing_product:
            for key, value in filtered_data.items():
                setattr(existing_product, key, value)
            target_product_id = existing_product.id
        else:
            new_product = Product(**filtered_data)
            session.add(new_product)
            await session.flush()
            target_product_id = new_product.id
        
        # 5. Save Comprehensive Analysis Result
        analysis_entry = AnalysisResult(
            product_id=target_product_id,
            profitability_score=analysis.get("profitability_score", 0),
            swot=analysis.get("swot", {}),
            score_breakdown=analysis.get("score_breakdown", {}),
            trend_analysis=analysis.get("trend_analysis", {}),
            competition_data=analysis.get("competition_data", {}), # If analyzer adds this
            feature_gaps={"gaps": blueprint.get("feature_gaps", [])},
            ai_recommendations=blueprint # Storing as dict
        )
        session.add(analysis_entry)
        logger.info(f"Analysis saved to DB for Product ID: {target_product_id}")

        # 6. Complete Job
        job.status = "completed"
        job.result_product_id = target_product_id
        job.completed_at = datetime.now()
        await session.commit()
        logger.info(f"Job {job.id} Completed Successfully")

    except Exception as e:
        logger.error(f"Job {job.id} Failed: {e}")
        job.status = "failed"
        job.error_message = str(e)
        await session.commit()

async def main():
    logger.info("Worker Service Started. Initializing...")
    logger.info(f"Database URL configured: {'Yes' if os.getenv('DATABASE_URL') else 'No'}")
    logger.info("Polling for jobs...")
    
    while True:
        try:
            async with AsyncSessionLocal() as session:
                # Poll for pending jobs with FOR UPDATE SKIP LOCKED
                # This ensures multiple workers can run without picking the same job
                query = (
                    select(ScrapingJob)
                    .where(ScrapingJob.status == "pending")
                    .order_by(ScrapingJob.created_at.asc())
                    .limit(1)
                    .with_for_update(skip_locked=True)
                )
                result = await session.execute(query)
                job = result.scalars().first()
                
                if job:
                    await process_job(job, session)
                else:
                    await asyncio.sleep(2) # Wait before next poll

        except Exception as e:
            logger.error(f"Polling Error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
