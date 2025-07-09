import asyncio
from app.db.session import engine
from app.db.base import Base

# add all tables for db creation
from app.models import user, configuration 

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init())