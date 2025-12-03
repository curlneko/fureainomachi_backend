from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.posts_model import Post
from app.schemas.users_schema import UserCreate, UserGet
from app.services.users_service import create_user_service

router = APIRouter()


@router.post("", response_model=UserGet)
def create_user(input: UserCreate, db: Session = Depends(get_db)) -> UserGet:
    new = create_user_service(db, input)
    return UserGet.model_validate(new)
