from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine
from app.schemas import UserResponse
from .models import User 
from python_helpers.validators  import is_valid_email
import httpx

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
    if not is_valid_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    existing = db.query(models.User).filter_by(email=user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = models.User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    try:
        response = httpx.post(
            "http://nginx/socket/notify",
            json={"message": f"User created: {user.email}"},
            timeout=5
        )
        response.raise_for_status()
        print("✅ WebSocket notification sent:", response.text)
    except httpx.RequestError as e:
        print("❌ Request error sending WS notification:", repr(e))
    except httpx.HTTPStatusError as e:
        print("❌ HTTP error from WS notification:", repr(e))
    except Exception as e:
        print("❌ Unexpected WS error:", repr(e))

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