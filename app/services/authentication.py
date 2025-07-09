from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.utils.security import hash_password
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from fastapi import Security
from app.core.config import settings

security = HTTPBearer()

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

async def currentUserID(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid or expired token")