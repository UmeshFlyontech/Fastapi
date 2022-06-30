from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog.models import User
from .. import database, schemas, models
from ..hashing import Hash


def create(db:Session, request: schemas.User):
    # hashed_password = pwd_context.hash(request.password) this can be used instead creating class for hashed password
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user

def get_all(db: Session):
    user = db.query(models.User).all()
    return user

def destroy(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    user.delete(synchronize_session=False)
    db.commit()
    return "User has been deleted successfully!"