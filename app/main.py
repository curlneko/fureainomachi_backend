import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from dotenv import load_dotenv
from fastapi import FastAPI

from app.db.database import Base, engine
from app.db.seed import init_dummy_data
from app.routers.posts_router import router as posts_router
from app.routers.users_router import router as users_router

# .env ファイルの内容を読み込む
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # modelsに定義されたテーブルを作成
    Base.metadata.create_all(bind=engine)

    # Dummy データ投入
    if os.getenv("ENV") == "DEV":
        init_dummy_data()

    # アプリ起動時の処理
    yield

    # アプリ終了時の処理
    print("アプリ終了: DB コネクションやバックグラウンドタスクを閉じます")
    engine.dispose()


app = FastAPI(title="Fureainomachi API", version="0.1.0", lifespan=lifespan)


app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/users", tags=["users"])
