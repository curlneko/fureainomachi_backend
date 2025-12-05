import pytest
from fastapi import Body, FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient

from app.core.error_handlers import (
    global_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)


def create_test_app() -> FastAPI:
    app = FastAPI()

    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

    @app.get("/http-exception")
    def raise_http_exception() -> None:
        raise HTTPException(status_code=404, detail="Item not found")

    @app.get("/validation-exception")
    def raise_validation_exception(email: str = Body(...)) -> dict[str, str]:
        # Bodyでemailを必須にする
        return {"email": email}

    @app.get("/general-exception")
    def raise_general_exception() -> None:
        raise Exception("Something went wrong")

    return app


def get_test_client() -> TestClient:
    app = create_test_app()
    return TestClient(app, raise_server_exceptions=False)


def test_http_exception_handler() -> None:
    client = get_test_client()

    res = client.get("/http-exception")
    assert res.status_code == 404
    assert res.json() == {"message": "Item not found", "status": "error"}


def test_validation_exception_handler() -> None:
    client = get_test_client()

    # emailを渡さずにリクエストを送信してバリデーションエラーを発生させる
    res = client.get("/validation-exception")
    print(res.json())
    assert res.status_code == 422
    assert res.json() == {
        "message": "[{'type': 'missing', 'loc': ('body',), 'msg': 'Field required', 'input': None}]",
        "status": "error",
    }


def test_global_exception_handler() -> None:
    client = get_test_client()

    res = client.get("/general-exception")
    assert res.status_code == 500
    assert res.json() == {"message": "Internal Server Error", "status": "error"}
