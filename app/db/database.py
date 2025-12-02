import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# .env ファイルの内容を読み込む
load_dotenv()

DB_URL = os.environ["DATABASE_URL"]

# SQLAlchemy エンジン作成
# 実行されるSQLをログに出力する
# SQLAlchemy 2.0 スタイル（より明確なAPI）で動作する
engine = create_engine(DB_URL, echo=True, future=True)

# セッション作成
# 明示的にコミットしない限り変更は確定されない
# セッションに追加したオブジェクトは、明示的にcommitするまで自動でDBに反映されない
# どのデータベース(↑engine)に接続するかを指定
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Baseクラス（モデル作成用）、ORMモデル（テーブルクラス）の基底クラス
class Base(DeclarativeBase):
    pass


# DBセッション依存関数
def get_db() -> Generator[Session, None, None]:
    # SQLAlchemy のセッションを作成
    db = SessionLocal()
    try:
        # yield でセッションを渡し、この関数を呼んだ先で db を使えるように渡す
        yield db
    finally:
        # 処理が終わったら必ずセッションを閉じる
        db.close()
