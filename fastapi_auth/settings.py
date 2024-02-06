# from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    jwt_secret_key: str

settings = Settings()

# class Settings(BaseModel):
#     authjwt_secret_key: str = "secret"
#     # Configure application to store and get JWT from cookies
#     authjwt_token_location: set = {"cookies"}
#     # Disable CSRF Protection for this example. default is True
#     authjwt_cookie_csrf_protect: bool = False
