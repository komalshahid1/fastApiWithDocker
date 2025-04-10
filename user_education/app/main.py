from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import exists
from . import models, schemas
from .database import engine, get_db

# Only create the user_educations table
models.UserEducation.__table__.create(bind=engine, checkfirst=True)

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# User Education endpoints
 # Make sure this import exists

import requests

@app.post("/user-education", response_model=schemas.UserEducation)
def create_user_education(user_education: schemas.UserEducationCreate, db: Session = Depends(get_db)):
    # Make API call to user service
    user_service_url = f"http://client_service:8001/users/{user_education.user_id}"
    response = requests.get(user_service_url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="User not found")

    db_user_education = models.UserEducation(**user_education.dict())
    db.add(db_user_education)
    db.commit()
    db.refresh(db_user_education)
    return db_user_education



@app.get("/user-education/{user_id}", response_model=list[schemas.UserEducation])
def get_user_educations(user_id: int, db: Session = Depends(get_db)):
    user_educations = db.query(models.UserEducation).filter(models.UserEducation.user_id == user_id).all()
    if not user_educations:
        raise HTTPException(status_code=404, detail="No education records found for this user")
    return user_educations

@app.get("/user-education/{user_id}/{education_id}", response_model=schemas.UserEducation)
def get_user_education(user_id: int, education_id: int, db: Session = Depends(get_db)):
    user_education = db.query(models.UserEducation).filter(
        models.UserEducation.user_id == user_id,
        models.UserEducation.id == education_id
    ).first()
    if not user_education:
        raise HTTPException(status_code=404, detail="Education record not found")
    return user_education 