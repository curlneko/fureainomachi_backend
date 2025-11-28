# fureainomachi_backend

## 開発環境の起動
VS Codeを開き、「> Dev Containers: Reopen in Container」

## 環境設定
pip install --user -r requirements.txt

## サーバー起動
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

## API
### Redoc
http://127.0.0.1:8000/redoc
### Swagger
http://127.0.0.1:8000/docs
### OpenAPI
http://127.0.0.1:8000/openapi.json