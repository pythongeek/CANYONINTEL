import asyncio
import sys
import os
from sqlalchemy import select, delete

# Add /app to path
sys.path.append('/app')

from app.database import AsyncSessionLocal
from app.models.job import ScrapingJob
from app.models.product import Product
from sqlalchemy import text

async def manual_ops():
    async with AsyncSessionLocal() as session:
        print("Cleaning failed/pending jobs...")
        # Delete failed jobs
        stmt = delete(ScrapingJob).where(ScrapingJob.status == "failed")
        await session.execute(stmt)
        
        # Delete pending jobs to clear queue
        stmt = delete(ScrapingJob).where(ScrapingJob.status == "pending")
        await session.execute(stmt)
        
        await session.commit()
        print("Cleaned jobs.")

        print("Seeding new valid job...")
        new_job = ScrapingJob(
            url="https://codecanyon.net/item/worksuite-saas-project-management-system/23263302",
            status="pending"
        )
        session.add(new_job)
        await session.commit()
        print(f"Seeded job for: {new_job.url}")

if __name__ == "__main__":
    asyncio.run(manual_ops())
