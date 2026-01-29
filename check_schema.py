import asyncio
from app.database import engine
from sqlalchemy import inspect

async def check_schema():
    async with engine.connect() as conn:
        columns = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_columns('analysis_results'))
        print(f"Columns in analysis_results: {[c['name'] for c in columns]}")

if __name__ == "__main__":
    asyncio.run(check_schema())
