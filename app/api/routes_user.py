from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserOut, UserPost, UserPut
from app.services import user as svc_user

router = APIRouter()

label = "User"

@router.get("/", response_model=list[UserOut], summary=f"{label} list")
async def index(db: AsyncSession = Depends(get_db)):
    return await svc_user.index(db)

@router.post("/", response_model=UserOut, summary=f"Insert new {label}")
async def post(user: UserPost, db: AsyncSession = Depends(get_db)):
    return await svc_user.post(db, user)

@router.get("/{id}", response_model=UserOut, summary=f"Get {label} details")
async def get(id: int, db: AsyncSession = Depends(get_db)):
    user = await svc_user.get(db, id)
    if not user:
        raise HTTPException(status_code=404, detail=f"{label} not found")
    return user

@router.put("/{id}", response_model=UserOut, summary=f"Update {label}")
async def put(id: int, user_update: UserPut, db: AsyncSession = Depends(get_db)):
    user = await svc_user.put(db, id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail=f"{label} not found")
    return user