from fastapi import FastAPI
from handlers.project_handler import router

def get_application() -> FastAPI:
    application = FastAPI(title="Project IS")
    application.include_router(router, prefix="")
    return application


app = FastAPI()