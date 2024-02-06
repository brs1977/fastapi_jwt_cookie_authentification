from async_fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException

from .model import Success, User

router = APIRouter()

@router.post("/login")
async def login(user: User, security: AuthJWT = Depends()) -> Success:
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    # Create the tokens and passing to set_access_cookies or set_refresh_cookies
    access_token = await security.create_access_token(subject=user.username)
    refresh_token = await security.create_refresh_token(subject=user.username)

    # Set the JWT cookies in the response
    await security.set_access_cookies(access_token)
    await security.set_refresh_cookies(refresh_token)
    return Success()


@router.post("/refresh")
async def refresh(security: AuthJWT = Depends()) -> Success:
    await security.jwt_refresh_token_required()

    current_user = await security.get_jwt_subject()
    new_access_token = await security.create_access_token(subject=current_user)
    # Set the JWT cookies in the response
    await security.set_access_cookies(new_access_token)
    return Success()


@router.delete("/logout")
async def logout(security: AuthJWT = Depends()) -> Success:
    await security.jwt_required()

    await security.unset_jwt_cookies()
    return Success()


@router.get("/protected")
async def protected(security: AuthJWT = Depends()) -> dict:
    await security.jwt_required()

    current_user = await security.get_jwt_subject()
    return {"user": current_user}
