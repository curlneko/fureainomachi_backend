from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.response import ResponseModel, success_response
from app.db.database import get_db
from app.models.posts_model import Post
from app.schemas.posts_schema import PostCreate, PostGet
from app.services.posts_service import create_post_service, get_posts_service

router = APIRouter()


@router.get("", response_model=ResponseModel)
def get_posts(db: Session = Depends(get_db)) -> ResponseModel:
    posts = get_posts_service(db)
    return success_response([PostGet.model_validate(p) for p in posts])


@router.post("", response_model=ResponseModel, status_code=201)
def create_post(post: PostCreate, db: Session = Depends(get_db)) -> ResponseModel:
    new_post = create_post_service(db, post)
    return success_response(PostGet.model_validate(new_post))
