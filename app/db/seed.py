from app.db.database import SessionLocal
from app.db.dummy_data.posts import dummy_posts
from app.db.dummy_data.users import dummy_users
from app.models.posts_model import Post
from app.models.users_model import User


def init_dummy_data() -> None:
    db = SessionLocal()
    try:
        if not db.query(Post).first():
            db.add_all(dummy_posts)

        if not db.query(User).first():
            db.add_all(dummy_users)

        db.commit()
    finally:
        db.close()
