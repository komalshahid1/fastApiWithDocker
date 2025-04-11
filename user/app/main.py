from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine
from app.schemas import UserResponse
from .models import User 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"service": "user"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter_by(email=user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = models.User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    try:
        return db.query(models.User).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = User.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user