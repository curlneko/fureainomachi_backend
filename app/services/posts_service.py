from sqlalchemy.orm import Session
from app.models.posts_model import Post
from app.schemas.posts_schema import PostCreate


def get_posts_service(db: Session):
    return db.query(Post).all()


def create_post_service(db: Session, post: PostCreate):
    # Pydantic モデルを dict に変換
    db_post = Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
