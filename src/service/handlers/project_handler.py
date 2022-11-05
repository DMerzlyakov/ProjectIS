from fastapi import APIRouter, Depends

from src.data.entity.models import Role
from src.data.repository.project_repository import connect_db
from src.config.config import *
router = APIRouter()


@router.get("/")
async def root(database=Depends(connect_db)):
    role_list = database.query(Role).all()
    return role_list
