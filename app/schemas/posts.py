from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

    # ← SQLAlchemyの結果をPydanticが受け取れる
    class Config:
        orm_mode = True
