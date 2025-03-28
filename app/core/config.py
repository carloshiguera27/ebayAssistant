from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "eBay Assistant API"
    debug: bool = True
    env: str = "development"
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()
