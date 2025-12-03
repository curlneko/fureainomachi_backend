from sqlalchemy import JSON, Column, Date, Integer, String

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    current_country = Column(String)
    birth_country = Column(String)
    gender = Column(String)
    spoken_language = Column(JSON)
    learning_language = Column(JSON)
    birthday = Column(Date)
