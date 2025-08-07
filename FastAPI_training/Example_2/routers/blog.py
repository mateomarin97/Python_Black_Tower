from fastapi import APIRouter, Depends, status, Response, HTTPException
from FastAPI_training.Example_2 import schemas, models
from FastAPI_training.Example_2.database import get_db
from sqlalchemy.orm import Session
from typing import List
from FastAPI_training.Example_2.repository import blog
from FastAPI_training.Example_2.oauth2 import get_current_token

router = APIRouter(prefix="/blog", tags=["Blogs"])

@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db), current_token: schemas.TokenData = Depends(get_current_token)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_token: schemas.TokenData = Depends(get_current_token)):
    user_id = db.query(models.User).filter(models.User.email == current_token.username).first().id
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return blog.create(request, db, user_id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_token: schemas.TokenData = Depends(get_current_token)):
    return blog.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_token: schemas.TokenData = Depends(get_current_token)):
    return blog.update(id, request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= schemas.ShowBlog)
def get_blog(id: int,db: Session = Depends(get_db), current_token: schemas.TokenData = Depends(get_current_token)):
   return blog.get(id, db)