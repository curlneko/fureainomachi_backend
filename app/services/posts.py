from sqlalchemy.orm import Session
from app.models.posts import Post


def get_posts(db: Session):
    return db.query(Post).all()
