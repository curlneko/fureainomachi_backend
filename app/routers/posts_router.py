from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db


from app.schemas.posts_schema import PostCreate, PostGet
from app.services.posts_service import get_posts_service, create_post_service

router = APIRouter()


@router.get("", response_model=list[PostGet])
def get_posts(db: Session = Depends(get_db)):
    posts = get_posts_service(db)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return posts


@router.post("", response_model=PostGet)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = create_post_service(db, post)
    return new_post
