from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.posts_model import Post
from app.schemas.posts_schema import PostCreate, PostGet
from app.services.posts_service import create_post_service, get_posts_service

router = APIRouter()


@router.get("", response_model=list[PostGet])
def get_posts(db: Session = Depends(get_db)) -> list[PostGet]:
    posts = get_posts_service(db)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return [PostGet.model_validate(p) for p in posts]


@router.post("", response_model=PostGet)
def create_post(post: PostCreate, db: Session = Depends(get_db)) -> PostGet:
    new_post = create_post_service(db, post)
    return PostGet.model_validate(new_post)
