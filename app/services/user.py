from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

async def get_user_by_name(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()

async def get_user(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)

async def get_users(db: AsyncSession): 
    result = await db.execute(select(User)) 
    return result.scalars().all() 

async def create_user(db: AsyncSession, user: UserCreate):
    hashed = hash_password(user.password)
    data = user.model_dump(exclude={"password"})
    db_user = User(**data, password=hashed)
    db.add(db_user) 
    await db.commit() 
    await db.refresh(db_user) 
    return db_user

async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate):
    db_user = await db.get(User, user_id)
    if not db_user:
        return None

    update_data = user_update.model_dump(exclude_unset=True) 
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    for field, value in update_data.items():
        setattr(db_user, field, value)

    await db.commit()
    await db.refresh(db_user)
    return db_user