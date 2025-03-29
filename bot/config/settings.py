from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(alias="BOT_TOKEN")

    class Config:
        env_file = ".env"