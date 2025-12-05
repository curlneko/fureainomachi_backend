from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.responses import Response

from app.core.logger import logger
from app.core.response import error_response


async def http_exception_handler(request: Request, exc: Exception) -> Response:
    if isinstance(exc, HTTPException):
        logger.warning(f"HTTPException: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content=error_response(exc.detail).model_dump(),
        )

    return JSONResponse(
        status_code=500,
        content=error_response("Unexpected HTTP exception").model_dump(),
    )


async def validation_exception_handler(request: Request, exc: Exception) -> Response:
    logger.warning(f"Validation error: {str(exc)}")
    return JSONResponse(status_code=422, content=error_response(str(exc)).model_dump())


async def global_exception_handler(request: Request, exc: Exception) -> Response:
    logger.critical(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500, content=error_response("Internal Server Error").model_dump()
    )
