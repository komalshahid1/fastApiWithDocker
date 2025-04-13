from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: str #EmailStr for email validation

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True
