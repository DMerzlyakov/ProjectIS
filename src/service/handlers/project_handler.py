from fastapi import APIRouter, Depends

from src.data.entity.models import *
from src.data.repository.project_repository import connect_db
from src.service.use_case.project_use_case import get_vacancy_list

router = APIRouter()

@router.get("/project/{project_id}")
async def root(project_id, database=Depends(connect_db)):
    project_list = database.query(Projects).filter(Projects.id == project_id).one_or_none()
    if project_list:
        return project_list
    else:
        return "Проект не найден"


@router.get("/project/{project_id}/vacancy")
async def root(project_id, database=Depends(connect_db)):
    project_id = database.query(Projects).filter(Projects.id == project_id).one_or_none()
    return get_vacancy_list(database, project_id)


@router.get("/projects")
async def root(database=Depends(connect_db)):
    project_id = database.query(Projects).all()
    return project_id
