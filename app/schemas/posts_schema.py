from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    content: str
    author_id: int


class PostCreate(PostBase):
    pass


class PostGet(PostBase):
    id: int

    # SQLAlchemyの結果をPydanticが受け取れる
    model_config = ConfigDict(from_attributes=True)
