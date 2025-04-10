from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship
from .database import Base

# Declare a minimal users table for FK reference (no real model needed)
# This is only for Alembic to resolve the ForeignKey
users = Table(
    "users",
    Base.metadata,
    Column("id", Integer, primary_key=True),
)

class UserEducation(Base):
    __tablename__ = "user_educations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course = Column(String(255), nullable=False)
    class_name = Column(String(255), nullable=False)
