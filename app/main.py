from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers.posts import router as posts_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fureainomachi API", version="0.1.0")

app.include_router(posts_router, prefix="/posts", tags=["posts"])
