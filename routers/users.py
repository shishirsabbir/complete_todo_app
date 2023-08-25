# importing packages
from fastapi import APIRouter, Depends, HTTPException, Path
from database import SessionLocal, Todos, Users
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext


# creating the fastapi instance called app
router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# for changing password for users
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# create database dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


# user dependency for jwt authorization
user_dependency = Annotated[dict, Depends(get_current_user)]


# pydantic class for user verification
class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


# create all routers
@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    
    return db.query(Users).filter(Users.id == user.get("id")).first()


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    
    user_model = db.query(Users).filter(Users.id == user.get("id")).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error on password change")
    
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)

    db.add(user_model)
    db.commit()
