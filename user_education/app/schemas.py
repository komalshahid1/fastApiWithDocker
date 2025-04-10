from pydantic import BaseModel, EmailStr

class UserEducationCreate(BaseModel):
    user_id: int
    course: str
    class_name: str

class UserEducation(UserEducationCreate):
    id: int

    class Config:
        from_attributes = True 