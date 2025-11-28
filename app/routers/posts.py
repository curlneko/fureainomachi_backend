from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db


from app.schemas.posts import Post
from app.services.posts import get_posts

router = APIRouter()


@router.get("/posts", response_model=list[Post])
def get_posts(db: Session = Depends(get_db)):
    posts = get_posts(db)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return posts
