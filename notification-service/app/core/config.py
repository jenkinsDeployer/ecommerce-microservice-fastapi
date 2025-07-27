from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_BROKER_URL: str
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = ".env"

settings = Settings()
