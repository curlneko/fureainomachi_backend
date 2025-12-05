from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.users_model import User
from app.schemas.users_schema import UserCreate


def create_user_service(db: Session, input: UserCreate) -> User:
    # Pydantic モデルを dict に変換

    logger.info(f"Creating user with email: {input.email}")

    db_input = User(**input.model_dump())
    db.add(db_input)
    db.commit()
    db.refresh(db_input)

    logger.success(f"User created with ID: {db_input.id}")
    return db_input
