from typing import Any

from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    result: Any | None
    message: Any | None


def success_response(data: Any) -> ResponseModel:
    return ResponseModel(status="success", result=data, message=None)


def error_response(message: Any) -> ResponseModel:
    return ResponseModel(status="error", result=None, message=message)
