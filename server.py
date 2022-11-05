from fastapi import FastAPI
from src.service.handlers.project_handler import router
from src.config.config import *


def get_application() -> FastAPI:
    application = FastAPI(title="Project IS")
    application.include_router(router)
    return application


app = get_application()


