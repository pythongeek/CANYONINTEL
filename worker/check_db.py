import asyncio
import os
import sys
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from dotenv import load_dotenv

# Ensure we can import from app
sys.path.append(os.getcwd())
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("ERROR: DATABASE_URL not found env")
    sys.exit(1)

# Fix for asyncpg
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

if "?sslmode=" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.split("?sslmode=")[0]

print(f"Connecting to: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else 'LOCAL'}...")

async def check():
    try:
        engine = create_async_engine(DATABASE_URL)
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT count(*) FROM scraping_jobs WHERE status = 'pending'"))
            count = result.scalar()
            print(f"SUCCESS! Connected to DB. Pending Jobs: {count}")
            
            # Also check if there are ANY jobs
            result = await conn.execute(text("SELECT count(*) FROM scraping_jobs"))
            total = result.scalar()
            print(f"Total Jobs in DB: {total}")
            
    except Exception as e:
        print(f"FAILURE: {e}")

if __name__ == "__main__":
    asyncio.run(check())
