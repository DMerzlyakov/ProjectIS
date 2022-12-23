from pydantic import Field
# DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/pro_db"
DATABASE_URL = Field(..., env='DATABASE_URL')
TITLE_PROJECT = "Project IS"
API_PREFIX = "/api"