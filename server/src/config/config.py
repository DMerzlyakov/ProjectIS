from pydantic import Field, BaseSettings

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/pro_db"
TITLE_PROJECT = "Project IS"
API_PREFIX = "/api"


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')


settings = Settings()
