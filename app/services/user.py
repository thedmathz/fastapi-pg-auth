from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserPost, UserPut
from app.utils.security import hash_password

async def index(db: AsyncSession): 
    result = await db.execute(select(User)) 
    return result.scalars().all() 

async def post(db: AsyncSession, user: UserPost):
    data = user.model_dump(exclude={"password"})
    db_user = User(**data, password=hash_password(user.password))
    db.add(db_user) 
    await db.commit() 
    await db.refresh(db_user) 
    return db_user

async def get(db: AsyncSession, id: int):
    return await db.get(User, id)

async def put(db: AsyncSession, id: int, user_update: UserPut):
    db_user = await db.get(User, id)
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