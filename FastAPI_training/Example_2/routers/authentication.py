from fastapi import APIRouter, Depends, status, HTTPException
from FastAPI_training.Example_2 import schemas, models
from FastAPI_training.Example_2.database import get_db
from FastAPI_training.Example_2.hashing import Hash
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from FastAPI_training.Example_2.JWTtoken import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token, status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    actual_user = db.query(models.User).filter(models.User.email == request.username).first()
    if not actual_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    actual_password = actual_user.password
    is_correct = Hash.verify(request.password, actual_password)
    if not is_correct:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    #generate a JWT token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": request.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")