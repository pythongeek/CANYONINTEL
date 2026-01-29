import asyncio
from app.database import engine
from sqlalchemy import text

async def test_conn():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print(f"Connection Successful: {result.fetchone()}")
    except Exception as e:
        print(f"Connection Failed: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_conn())
