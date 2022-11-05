import datetime

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from src.config.config import *
from src.data.entity.models import Projects, Skills, Vacancies, VacanciesProject, Role


def connect_db():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())
    return session


"""
To Next Release
"""
# def update_base(engine):
#     data_for_projects = [{'owner': 'Давид', 'manager': 'Данила', 'startDate': datetime.datetime.utcnow(),
#                           'endDate': datetime.datetime.utcnow(), 'title': 'Разработка', 'price': 20000, 'status': 'В работе'},
#                          {'owner': 'Даша', 'manager': 'Никита', 'startDate': datetime.datetime.utcnow(),
#                           'endDate': datetime.datetime.utcnow(), 'title': 'Python-разработка', 'price': 500000, 'status': 'Завершено'}]
#     data_for_role = [{'title':'python-developer', 'grade': 2}, {'title':'java-developer', 'grade':3}]
#     data_for_skills = [{'title':'English', 'level': 2}, {'title': 'Web-development', 'level': 3}]
#     data_for_vacancies = [{'type': 'Python-developer', 'role_id': 1, 'skill_id': 1}, {'type': 'java-developer', 'role_id': 2, 'skill_id': 2}]
#     data_for_vacanciesProject = [{'project_id': 1, 'vacancy_id': 1}, {'project_id': 2, 'vacancy_id': 2}]
#
#     engine.execute(insert(Projects, data_for_projects))
#     engine.execute(insert(Skills, data_for_skills))
#     engine.execute(insert(Vacancies, data_for_vacancies))
#     engine.execute(insert(Role, data_for_vacancies))
#     engine.execute(insert(VacanciesProject, data_for_vacanciesProject))
