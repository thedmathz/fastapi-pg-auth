from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.core.security import hash_password

async def get_user_by_name(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none() 

async def create_administrator(db: AsyncSession):
    username = 'admin'
    db_user = User(
        username=username, 
        password=hash_password(username), 
        fname=username.title(), 
        mname='', 
        lname=username.title(), 
        gender='Male', 
    )
    db.add(db_user) 
    await db.commit() 
    await db.refresh(db_user) 
    return db_user