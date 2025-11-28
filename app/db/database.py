from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "postgresql://user:password@db:5432/fureainomachi"

# SQLAlchemy エンジン作成
engine = create_engine(DB_URL, echo=True, future=True)

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baseクラス（モデル作成用）
Base = declarative_base()


# DBセッション依存関数
def get_db():
    # SQLAlchemy のセッションを作成
    db = SessionLocal()
    try:
        # yield でセッションを渡し、この関数を呼んだ先で db を使えるように渡す
        yield db
    finally:
        # 処理が終わったら必ずセッションを閉じる
        db.close()
