from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.configuration import Configuration
from app.schemas.configuration import ConfigurationPost, ConfigurationPut

async def index(db: AsyncSession): 
    result = await db.execute( select(Configuration).where(Configuration.status == 1) )
    return result.scalars().all()

async def post(db: AsyncSession, configuration: ConfigurationPost):
    data = configuration.model_dump()
    db_configuration = Configuration(**data)
    db.add(db_configuration) 
    await db.commit() 
    await db.refresh(db_configuration) 
    return db_configuration

async def get(db: AsyncSession, id: int): 
    return await db.get(Configuration, id) 

async def put(db: AsyncSession, id: int, configuration_update: ConfigurationPut):
    db_configuration = await db.get(Configuration, id)
    if not db_configuration:
        return None

    update_data = configuration_update.model_dump(exclude_unset=True) 
    for field, value in update_data.items():
        setattr(db_configuration, field, value)

    await db.commit()
    await db.refresh(db_configuration)
    return db_configuration

async def delete(db: AsyncSession, id: int):
    db_configuration = await db.get(Configuration, id)
    if not db_configuration:
        return None

    await db.delete(db_configuration)
    await db.commit()
    return db_configuration