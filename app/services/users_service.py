from sqlalchemy.orm import Session

from app.models.users_model import User
from app.schemas.users_schema import UserCreate


def create_user_service(db: Session, input: UserCreate) -> User:
    # Pydantic モデルを dict に変換
    db_input = User(**input.model_dump())
    db.add(db_input)
    db.commit()
    db.refresh(db_input)
    return db_input
