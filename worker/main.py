import asyncio
import os
import logging
import json
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update
from datetime import datetime

# Import models - Assuming app/models is accessible
# We need to ensure PYTHONPATH includes root
import sys
sys.path.append(os.getcwd())

from app.models.job import ScrapingJob
from app.models.product import Product
from worker.scraper import PlaywrightScraper
from worker.analyzer import MarketAnalyzer

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CanyonWorker")

# Database Setup
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found")

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def process_job(job: ScrapingJob, session: AsyncSession):
    """Executes the full pipeline for a single job."""
    logger.info(f"Processing Job {job.id} - {job.url}")
    
    try:
        # 1. Update Status -> Processing
        stmt = update(ScrapingJob).where(ScrapingJob.id == job.id).values(status="processing")
        await session.execute(stmt)
        await session.commit()

        # 2. Scrape (Playwright)
        scraper = PlaywrightScraper(headless=True)
        raw_data = await scraper.scrape(job.url)
        logger.info(f"Scraped Data: {raw_data['title']}")

        # 3. Analyze (Gemini)
        analyzer = MarketAnalyzer()
        analysis = await analyzer.analyze_product(raw_data)
        
        # Merge Analysis into Data (stored in description or features for now)
        # Or ideally store in JSON field. For now, append to description.
        raw_data["description"] += f"\n\n[AI ANALYSIS]\nVerdict: {analysis['verdict']}\nScore: {analysis['profitability_score']}\nSaturation: {analysis['market_saturation']}"

        # 4. Save Product
        # ID check
        prod_stmt = select(Product).where(Product.codecanyon_id == str(raw_data.get('codecanyon_id', '')))
        # Note: scraper might not extract ID yet.
        # Fallback: Check by Title or URL
        
        # Create or Update Product logic (Simplified)
        new_product = Product(**raw_data)
        session.add(new_product)
        await session.flush()
        
        # 5. Complete Job
        stmt = update(ScrapingJob).where(ScrapingJob.id == job.id).values(
            status="completed",
            result_product_id=new_product.id,
            completed_at=datetime.now()
        )
        await session.execute(stmt)
        await session.commit()
        logger.info(f"Job {job.id} Completed Successfully")

    except Exception as e:
        logger.error(f"Job {job.id} Failed: {e}")
        stmt = update(ScrapingJob).where(ScrapingJob.id == job.id).values(
            status="failed",
            error_message=str(e)
        )
        await session.execute(stmt)
        await session.commit()

async def main():
    logger.info("Worker Service Started. Polling for jobs...")
    
    while True:
        try:
            async with AsyncSessionLocal() as session:
                # Poll for pending jobs
                query = select(ScrapingJob).where(ScrapingJob.status == "pending").limit(1)
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
