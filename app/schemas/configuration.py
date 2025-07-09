from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class ConfigurationBase(BaseModel):
    name: str
    value: str
    remarks: str

class ConfigurationPost(ConfigurationBase):
    insertedBy: int
    status: int = 1
    
class ConfigurationGet(ConfigurationBase):
    configurationID: int
    insertedBy: int
    dateInserted: Optional[datetime]
    updatedBy: int
    dateUpdated: Optional[datetime]
    status: int
    
    model_config = { "from_attributes": True }

class ConfigurationPut(ConfigurationBase):
    updatedBy: int
    dateUpdated: Optional[datetime] = datetime.now()
    status: int
    
class ConfigurationID(BaseModel):
    configurationID: int

    model_config = { "from_attributes": True }