import os
from pydantic import Field, PostgresDsn, RedisDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Core
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field("HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    DEBUG: bool = Field(False, env="DEBUG")

    @field_validator("DEBUG", mode="before")
    @classmethod
    def parse_bool(cls, v):
        if isinstance(v, str):
            return v.strip().lower() in ("true", "1", "yes")
        return v
    
    # API Keys
    GEMINI_API_KEY: Optional[str] = Field(None, env="GEMINI_API_KEY")
    
    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    # Helper to fix DATABASE_URL for asyncpg if needed
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        url = self.DATABASE_URL
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        # Remove sslmode if present, as it's handled in database.py for asyncpg
        if "sslmode=" in url:
            import re
            url = re.sub(r'[?&]sslmode=[^&]*', '', url)
        return url

    # Redis
    REDIS_URL: Optional[str] = Field(None, env="REDIS_URL")
    
    # Scraper
    SCRAPER_API_KEY: Optional[str] = Field(None, env="SCRAPER_API_KEY")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
