from app.db.database import SessionLocal
from app.models.posts_model import Post
from app.db.dummy_data.posts import dummy_posts


def init_dummy_data():
    db = SessionLocal()
    try:
        if not db.query(Post).first():
            db.add_all(dummy_posts)

        db.commit()
    finally:
        db.close()
