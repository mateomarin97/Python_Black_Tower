from fastapi import APIRouter, status, Depends, HTTPException
from FastAPI_training.Example_2 import schemas, models
from FastAPI_training.Example_2.database import  get_db
from sqlalchemy.orm import Session
from FastAPI_training.Example_2.hashing import Hash
from FastAPI_training.Example_2.repository import user

router = APIRouter(prefix= "/user" ,tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)