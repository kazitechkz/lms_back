from typing import Optional

from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings

load_dotenv()


class AppConfiguration(BaseSettings):
    app_name: str = Field(default="LMS", env="APP_NAME")
    app_description: str = Field(default="LMS DESCRIPTION", env="APP_DESCRIPTION")
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    app_debug: bool = Field(default=False, env="APP_DEBUG")
    app_docs_url: Optional[str] = Field(default=False, env="APP_DOCS_URL")
    app_redoc_url: Optional[str] = Field(default=False, env="APP_REDOC_URL")

    db_type: str = Field(..., env="DB_TYPE")
    db_connection: str = Field(..., env="DB_CONNECTION")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_password: Optional[str] = Field(..., env="DB_PASSWORD")
    db_pool_size: int = Field(..., env="DB_POOL_SIZE")
    db_max_overflow: int = Field(..., env="DB_MAX_OVERFLOW")
    db_pool_timeout: int = Field(..., env="DB_POOL_TIMEOUT")
    db_pool_recycle: int = Field(..., env="DB_POOL_RECYCLE")
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(..., env="ALGORITHM")
    access_token_expire_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_days: int = Field(..., env="REFRESH_TOKEN_EXPIRE_DAYS")

    app_status: str = Field(..., env="APP_STATUS")

    aws_access_key_id: str = Field(..., env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = Field(..., env="AWS_SECRET_ACCESS_KEY")
    aws_region_name: str = Field(..., env="AWS_REGION_NAME")
    aws_s3_bucket_name: str = Field(..., env="AWS_S3_BUCKET_NAME")

    google_client_id: str = Field(..., env="GOOGLE_CLIENT_ID")
    google_secret: str = Field(..., env="GOOGLE_SECRET")

    youtube_access_token: str = Field(..., env="YOUTUBE_ACCESS_TOKEN")
    youtube_refresh_token: str = Field(..., env="YOUTUBE_REFRESH_TOKEN")

    static_folder: str = "static"

    @property
    def get_db_url(self) -> str:
        return f"{self.db_connection}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @field_validator("db_type")
    def validate_app_database(cls, v):
        if v.lower() not in {"postgresql", "mysql"}:
            raise ValueError("APP_DATABASE must be 'postgresql' or 'mysql'")
        return v

    @field_validator("app_status")
    def validate_app_status(cls, v):
        if v.lower() not in {"development", "production"}:
            raise ValueError("APP_STATUS must be 'development' or 'production'")
        return v

    class Config:
        env_file = ".env"


# Загрузка конфигурации из.env-файла и создание экземпляра конфигурации
app_config = AppConfiguration()
