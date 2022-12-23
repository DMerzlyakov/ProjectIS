from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.config import *
from src.service.handlers.project_handler import router
from src.service.handlers.role_handler import router_role


def get_application() -> FastAPI:
    application = FastAPI(title=TITLE_PROJECT)

    origins = ["*"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(router, prefix=API_PREFIX)
    application.include_router(router_role, prefix=API_PREFIX)
    return application


app = get_application()

# uvicorn server:app

