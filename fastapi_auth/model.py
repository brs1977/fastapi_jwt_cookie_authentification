from pydantic import BaseModel


class AppModel(BaseModel):
    ...

class Success(AppModel):
    status: str = "Success"

class User(BaseModel):
    username: str
    password: str

class JwtSettings(AppModel):
    authjwt_secret_key: str = "secret"
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    # Disable CSRF Protection for this example. default is True
    authjwt_cookie_csrf_protect: bool = False
    cookie_max_age: int = 60
