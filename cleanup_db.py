import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not found in .env")
        return
    
    # Simple cleanup of postgresql:// to postgresql+asyncpg:// if needed
    # but asyncpg.connect likes the standard postgresql://
    if db_url.startswith("postgresql+asyncpg://"):
        db_url = db_url.replace("postgresql+asyncpg://", "postgresql://", 1)
    
    print(f"Connecting to database...")
    try:
        conn = await asyncpg.connect(db_url)
        print("Dropping alembic_version table...")
        await conn.execute("DROP TABLE IF EXISTS alembic_version;")
        print("Successfully cleared migration state.")
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
