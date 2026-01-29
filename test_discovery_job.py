import asyncio
import os
# from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.models.job import ScrapingJob

# load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("DATABASE_URL not found in env")
    exit(1)

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_test_job():
    url = "https://codecanyon.net/category/php-scripts?sort=sales"
    print(f"Creating test discovery job for: {url}")
    
    async with AsyncSessionLocal() as session:
        new_job = ScrapingJob(
            url=url,
            status="pending"
        )
        session.add(new_job)
        await session.commit()
        print(f"Job created with ID: {new_job.id}")

if __name__ == "__main__":
    asyncio.run(create_test_job())
