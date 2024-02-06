from async_fastapi_jwt_auth import AuthJWT
from async_fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .model import JwtSettings
from .router import router
from .settings import settings


def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

def create_app(_=None) -> FastAPI:

    app = FastAPI()
    app.include_router(router)

    app.exception_handler(AuthJWTException)(authjwt_exception_handler)

    return app


@AuthJWT.load_config
def get_config():
    return JwtSettings(authjwt_secret_key = settings.jwt_secret_key)

