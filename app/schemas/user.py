from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    username: str
    password: str
    
class UserBase(BaseModel):
    username: str
    fname: str
    mname: Optional[str] = ''
    lname: str
    gender: str

class UserPost(UserBase):
    password: str

class UserPut(BaseModel):
    fname: str
    lname: str
    password: str 
    
class UserOut(UserBase):
    userID: int

    model_config = {
        "from_attributes": True
    }