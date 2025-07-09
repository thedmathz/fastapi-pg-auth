from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserLogin
from app.services import authentication as svc_authentication
from app.core.security import verify_password

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
    return {"msg": "Login successful"}

@router.post("/verify", summary=f"Verify Token")
async def verify(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await svc_authentication.get_user_by_name(db, user_in.username)
    if not user or not verify_password(user_in.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": "Login successful"}

@router.post("/logout", summary=f"Log Out")
async def login(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await svc_authentication.get_user_by_name(db, user_in.username)
    if not user or not verify_password(user_in.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"msg": "Login successful"}
