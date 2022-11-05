from fastapi import FastAPI

from src.config.config import *
from src.service.handlers.project_handler import router


def get_application() -> FastAPI:
    application = FastAPI(title=TITLE_PROJECT)
    application.include_router(router, prefix=API_PREFIX)
    return application


app = get_application()


