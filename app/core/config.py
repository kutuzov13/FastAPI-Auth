import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
    DEBUG: bool = os.getenv('TESTING', False)
    API_TITLE: str = os.getenv('API_TITLE', 'FastAPI template')
    API_DESCRIPTION: str = 'Template for creating applications with FastAPI'
    API_VERSION: str = os.getenv('API_VERSION', '0.0.1')
    DATABASE_URL: AnyUrl = os.getenv('DATABASE_URL', 'sqlite://db.sqlite')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', 15436)
    POSTGRES_DB_NAME: str = os.getenv('POSTGRES_DB_NAME', 'postgres')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'postgres')

    SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@' \
                              f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}'


@lru_cache()
def get_setting() -> BaseSettings:
    """Get Base Settings and append in cache."""
    return Settings()


settings = Settings()