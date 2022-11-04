from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Boolean, create_engine
from sqlalchemy.orm import declarative_base, relationship
#import psycopg2

Base = declarative_base()


class Requests(Base):
    __tablename__ = 'requests'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=True)
    customer_id = Column(Integer, ForeignKey('employees.id'), nullable=True)
    create_date = Column(DATETIME)
    theme = Column(String)
    text = Column(String)
    done_date = Column(DATETIME)
    status = Column(String)


class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employees_role_id = Column(Integer, ForeignKey('employeesRole.id'))
    employees_skill_id = Column(Integer, ForeignKey('employeesSkills.id'))
    status_id = Column(Integer, ForeignKey('status.id'))
    lastName = Column(Integer)
    firstName = Column(Integer)
    secondName = Column(String)

class Status(Base):
    __tablename__ = 'status'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    startDate = Column(DATETIME)
    endDate = Column(DATETIME)
    active = Column(String)

class VacanciesProject(Base):
    __tablename__ = 'vacanciesProject'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))


class Vacancies(Base):
    __tablename__ = 'vacancies'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))


class Interviews(Base):
    __tablename__ = 'interviews'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    rookie_id = Column(Integer, ForeignKey('rookies.id'))
    rating = Column(Integer)


class done_projects(Base):
    __tablename__ = 'doneProjects'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner = Column(String)
    manager = Column(String)
    startDate = Column(DATETIME)
    endDate = Column(DATETIME)
    title = Column(String)
    price = Column(String)


class Projects(Base):
    __tablename__ = 'projects'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner = Column(String)
    manager = Column(String)
    startDate = Column(DATETIME)
    endDate = Column(DATETIME)
    title = Column(String)
    price = Column(Integer)
    status = Column(String)


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


class Rookies(Base):
    __tablename__ = 'rookies'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    skill_id = Column(Integer, ForeignKey('skill.id'))
    firstName = Column(String)
    lastName = Column(String)
    secondName = Column(String)
    vacancy_id = Column(Integer, ForeignKey('vacancies.id'))


class EmployeesSkills(Base):
    __tablename__ = 'employeesSkills'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill_id = Column(Integer, ForeignKey('skills.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))


class EmployeesRole(Base):
    __tablename__ = 'employeesRole'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
