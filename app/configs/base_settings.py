from enum import StrEnum

from pydantic_settings import BaseSettings


class Env(StrEnum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"


class Settings(BaseSettings):
    ENV: Env = Env.LOCAL
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "1234"
    DB_DB: str = "oz_fastapi2"
