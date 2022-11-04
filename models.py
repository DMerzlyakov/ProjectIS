from sqlalchemy import Column, Integer, String, ForeignKey, DATE, Boolean, create_engine, DATE
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    grade = Column(Integer)


class Skills(Base):
    __tablename__ = 'skills'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    level = Column(Integer)


class Vacancies(Base):
    __tablename__ = 'vacancies'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    role_id = Column(Integer, ForeignKey(Role.id))
    skill_id = Column(Integer, ForeignKey(Skills.id))


class Projects(Base):
    __tablename__ = 'projects'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner = Column(String)
    manager = Column(String)
    startDate = Column(DATE)
    endDate = Column(DATE)
    title = Column(String)
    price = Column(Integer)
    status = Column(String)


class done_projects(Base):
    __tablename__ = 'doneProjects'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner = Column(String)
    manager = Column(String)
    startDate = Column(DATE)
    endDate = Column(DATE)
    title = Column(String)
    price = Column(String)


class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    lastName = Column(Integer)
    firstName = Column(Integer)
    secondName = Column(String)


class Status(Base):
    __tablename__ = 'status'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey(Vacancies.id))
    employee_id = Column(Integer, ForeignKey(Employees.id))
    startDate = Column(DATE)
    endDate = Column(DATE)
    active = Column(String)


class EmployeesRole(Base):
    __tablename__ = 'employeesRole'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey(Role.id))
    employee_id = Column(Integer, ForeignKey(Employees.id))


class Requests(Base):
    __tablename__ = 'requests'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(Employees.id), nullable=True)
    customer_id = Column(Integer, ForeignKey(Employees.id), nullable=True)
    create_date = Column(DATE)
    theme = Column(String)
    text = Column(String)
    done_date = Column(DATE)
    status = Column(String)


class VacanciesProject(Base):
    __tablename__ = 'vacanciesProject'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey(Projects.id))
    vacancy_id = Column(Integer, ForeignKey(Vacancies.id))


class Rookies(Base):
    __tablename__ = 'rookies'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey(Role.id))
    skill_id = Column(Integer, ForeignKey(Skills.id))
    firstName = Column(String)
    lastName = Column(String)
    secondName = Column(String)
    vacancy_id = Column(Integer, ForeignKey(Vacancies.id))


class Interviews(Base):
    __tablename__ = 'interviews'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(Employees.id))
    rookie_id = Column(Integer, ForeignKey(Rookies.id))
    rating = Column(Integer)


class EmployeesSkills(Base):
    __tablename__ = 'employeesSkills'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill_id = Column(Integer, ForeignKey(Skills.id))
    employee_id = Column(Integer, ForeignKey(Employees.id))


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgrespw@localhost:49153/postgres')
    Base.metadata.create_all(engine)
