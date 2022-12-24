from src.data.entity.models import VacanciesProject, Vacancies


def get_vacancy_list(database, project_id):
    if project_id:
        id_list = [i.vacancy_id for i in database.query(VacanciesProject).all()]
        if id_list:
            vacancy_list = database.query(Vacancies).filter(Vacancies.id.in_(id_list)).all()
            return vacancy_list
        return "Вакансии проекта не найдены"
    else:
        return "Проект не найден"
