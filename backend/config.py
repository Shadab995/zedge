from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Starter"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8001


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb://127.0.0.1:27017/"
    DB_NAME: str = "test_auth_db"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()