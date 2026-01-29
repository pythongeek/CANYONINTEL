import asyncio
import os
from sqlalchemy import select
from app.database import AsyncSessionLocal
from app.models.user import User
from dotenv import load_dotenv

load_dotenv()

async def check():
    async with AsyncSessionLocal() as db:
        res = await db.execute(select(User).where(User.email == 'test8@example.com'))
        user = res.scalars().first()
        if user:
            print(f'User found: {user.email}')
        else:
            print('User not found')

if __name__ == "__main__":
    asyncio.run(check())
