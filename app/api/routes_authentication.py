from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserLogin
from app.services import authentication as svc_authentication
from app.utils.security import verify_password
from app.utils.token import create_access_token

router = APIRouter()

@router.get("/create-admin", summary=f"Create Admin")
async def create_admin(db: AsyncSession = Depends(get_db)):
    user = await svc_authentication.get_user_by_name(db, 'admin')
    if user:
        raise HTTPException(status_code=401, detail="Admin already exists.")
    await svc_authentication.create_administrator(db)
    return {"msg": "Admin successful created"}

@router.post("/login", summary=f"Log In")
async def login(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await svc_authentication.get_user_by_name(db, user_in.username)
    if not user or not verify_password(user_in.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(user.userID)})
    return {"access_token": access_token}