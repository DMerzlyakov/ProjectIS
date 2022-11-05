from fastapi import Depends, APIRouter

from src.data.entity.models import Role
from src.data.repository.project_repository import connect_db

router_role = APIRouter()


@router_role.get("/role/{role_id}")
async def root(project_id, database=Depends(connect_db)):
    role_list = database.query(Role).filter(Role.id == project_id).one_or_none()
    if role_list:
        return role_list
    else:
        return "Роль не найден"


@router_role.get("/roles")
async def root(database=Depends(connect_db)):
    role_list = database.query(Role).all()
    return role_list
