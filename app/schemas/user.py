from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    lname: str
    fname: str
    mname: str | None = None
    gender: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    userID: int

    model_config = {
        "from_attributes": True
    }

class UserLogin(BaseModel):
    username: str
    password: str
    
class UserUpdate(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None
    password: Optional[str] = None 