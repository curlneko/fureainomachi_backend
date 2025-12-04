from datetime import date

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.enums.country import Country
from app.enums.gender import Gender
from app.enums.language import Language
from app.utils.validate import (
    validate_birthday,
    validate_email,
    validate_input,
    validate_password,
)


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=8)
    current_country: Country
    birth_country: Country
    gender: Gender
    spoken_language: list[Language]
    learning_language: list[Language]
    birthday: date

    @field_validator("*", mode="before")
    def all_fields_check(cls, value: str | list[str]) -> str | list[str]:
        return validate_input(value)

    @field_validator("email")
    def email_check(cls, value: str) -> str:
        return validate_email(value)

    @field_validator("password")
    def password_check(cls, value: str) -> str:
        return validate_password(value)

    @field_validator("birthday")
    def birthday_check(cls, value: date) -> date:
        return validate_birthday(value)


class UserCreate(UserBase):
    pass


class UserGet(UserBase):
    id: int

    # SQLAlchemyの結果をPydanticが受け取れる
    model_config = ConfigDict(from_attributes=True)
