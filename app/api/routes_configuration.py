from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.configuration import ConfigurationID, ConfigurationPost, ConfigurationGet, ConfigurationPut
from app.services import configuration as svc_configuration
from app.services import authentication as svc_authentication

router = APIRouter()

label = 'Configuration'

@router.get("/", response_model=list[ConfigurationGet], summary=f"{label} list")
async def index(db: AsyncSession = Depends(get_db), userID: str = Depends(svc_authentication.currentUserID)):
    return await svc_configuration.index(db)

@router.post("/", response_model=ConfigurationID, summary=f"Insert new {label}")
async def post(configuration: ConfigurationPost, db: AsyncSession = Depends(get_db), userID: str = Depends(svc_authentication.currentUserID)):
    return await svc_configuration.post(db, configuration)

@router.get("/{id}", response_model=ConfigurationGet, summary=f"Get {label} details")
async def get(id: int, db: AsyncSession = Depends(get_db), userID: str = Depends(svc_authentication.currentUserID)):
    configuration = await svc_configuration.get(db, id)
    if not configuration:
        raise HTTPException(status_code=404, detail=f"{label} not found")
    return configuration

@router.put("/{id}", response_model=ConfigurationID, summary=f"Update {label}")
async def put(id: int, configuration_update: ConfigurationPut, db: AsyncSession = Depends(get_db), userID: str = Depends(svc_authentication.currentUserID)):
    configuration = await svc_configuration.put(db, id, configuration_update)
    if not configuration:
        raise HTTPException(status_code=404, detail=f"{label} not found")
    return configuration

@router.delete("/{id}", summary=f"Delete {label}")
async def delete(id: int, db: AsyncSession = Depends(get_db), userID: str = Depends(svc_authentication.currentUserID)):
    configuration = await svc_configuration.delete(db, id)
    if not configuration:
        raise HTTPException(status_code=404, detail=f"{label} not found")
    return {"detail": f"{label} deleted successfully"} 