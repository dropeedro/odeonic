from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    oauth_provider: Optional[str] = None  # Google, Facebook, etc.
    oauth_id: Optional[str] = None        # ID del OAuth

class UserResponse(BaseModel):
    id: str
    email: EmailStr

    class Config:
        orm_mode = True
