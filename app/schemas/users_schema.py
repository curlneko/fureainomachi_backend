from datetime import date

from pydantic import BaseModel, ConfigDict

from app.enums.country import Country
from app.enums.gender import Gender
from app.enums.language import Language


class UserBase(BaseModel):
    name: str
    email: str
    password: str
    current_country: Country
    birth_country: Country
    gender: Gender
    spoken_language: list[Language]
    learning_language: list[Language]
    birthday: date


class UserCreate(UserBase):
    pass


class UserGet(UserBase):
    id: int

    # SQLAlchemyの結果をPydanticが受け取れる
    model_config = ConfigDict(from_attributes=True)
