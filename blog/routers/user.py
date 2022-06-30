from fastapi import APIRouter, status, HTTPException, Depends
from blog.repository.user import create, show
from blog.routers.authentication import router
from .. import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from ..hashing import Hash
from typing import List
from ..repository import user


router = APIRouter(
    prefix = "/user",
    tags=["Users"]
)

# User repository is created to manage bigger applications and multiple files.
get_db = database.get_db

@router.post("/", response_model= schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return user.create(db, request)

@router.get("/{id}", status_code=200, response_model= schemas.ShowUser)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return user.show(id, db)

@router.get("/", response_model= List[schemas.ShowUser])
def all(db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return user.get_all(db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return user.destroy(id, db)