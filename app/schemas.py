from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[str] = "intern"

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class SubmissionCreate(BaseModel):
    title: str
    content: str

class SubmissionResponse(BaseModel):
    id: int
    title: str
    content: str
    status: str
    intern_id: int
    created_at: datetime

    class Config:
        from_attributes = True

