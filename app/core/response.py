from typing import Any, TypedDict


class ResponseModel(TypedDict, total=False):
    status: str
    result: Any | None
    message: Any | None


def success_response(data: Any) -> ResponseModel:
    return {"status": "success", "result": data}


def error_response(message: Any) -> ResponseModel:
    return {"status": "error", "message": message}
