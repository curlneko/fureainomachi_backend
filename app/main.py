import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.error_handlers import (
    global_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from app.db.database import Base, engine
from app.routers.posts_router import router as posts_router
from app.routers.users_router import router as users_router

# .env ファイルの内容を読み込む
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # アプリ起動時の処理
    yield

    # アプリ終了時の処理
    print("アプリ終了: DB コネクションやバックグラウンドタスクを閉じます")
    engine.dispose()


app = FastAPI(title="Fureainomachi API", version="0.1.0", lifespan=lifespan)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/users", tags=["users"])
