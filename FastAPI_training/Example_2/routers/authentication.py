from fastapi import APIRouter, Depends, status
from FastAPI_training.Example_2 import schemas
from FastAPI_training.Example_2.database import get_db
from FastAPI_training.Example_2.repository import authentication as auth_repo
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token, status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_repo.Generate_JWT_Token(request, db)