from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.posts_model import Post
from app.schemas.posts_schema import PostCreate


def get_posts_service(db: Session) -> list[Post]:
    return db.query(Post).all()


def create_post_service(db: Session, post: PostCreate) -> Post:
    # Pydantic モデルを dict に変換

    logger.info(f"Creating post with title: {post.title}")

    db_post = Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    logger.success(f"Post created with ID: {db_post.id}")
    return db_post
