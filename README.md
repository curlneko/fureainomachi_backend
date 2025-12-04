# fureainomachi_backend

## 開発環境の起動
VS Codeを開き、「> Dev Containers: Reopen in Container」

## 環境設定
pip install --user -r requirements.txt

## サーバー起動
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

## DBマイグレーション
### マイグレーションファイルを「作成」する
alembic revision --autogenerate -m "initial tables"
### マイグレーションファイルに書かれた内容を実際のデータベースに適用
alembic upgrade head
alembic -x echo=True upgrade head

### データの投入
python -m app.db.seed

## API
### Redoc
http://127.0.0.1:8000/redoc
### Swagger
http://127.0.0.1:8000/docs
### OpenAPI
http://127.0.0.1:8000/openapi.json

## テスト実装規則
### 単体テスト
services、routersはカバーレッジ100％

### 単体テスト実行
pytest -v --cov=app --cov-report=html --cov-report=term-missing tests/

## Makefile実行
black – コードフォーマッタ（自動整形）
isort – import 整理ツール
flake8 – Lint / コード品質チェック
mypy - 型チェック

### コード整形
make format

### Lint チェック
make lint

### 型チェック
make typecheck

### テスト + カバレッジ
make test

### まとめて全部実行(commit前かならず実行)
make all