from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Boolean, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Requests(Base):
    __tablename__ = 'requests'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(''), nullable=True)
    customer_id = Column(Integer, ForeignKey(''), nullable=True)
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
    role_id = Column(Integer, ForeignKey(''))
    skill_id = Column(Integer, ForeignKey(''))
    status_id = Column(Integer, ForeignKey(''))
    lastName = Column(Integer)
    firstName = Column(Integer)
    secondName = Column(String)

class Status(Base):
    __tablename__ = 'Status'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey(''))
    employee_id = Column(Integer, ForeignKey(''))
    startDate = Column(DATETIME)
    endDate = Column(DATETIME)
    active = Column(String)

class VacanciesProject(Base):
    __tablename__ = 'vacanciesProject'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey(''))
    vacancy_id = Column(Integer, ForeignKey(''))


class Vacancies(Base):
    __tablename__ = 'vacancies'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    role_id = Column(Integer, ForeignKey(''))
    skill_id = Column(Integer, ForeignKey(''))


class Interviews(Base):
    __tablename__ = 'interviews'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey(''))
    rookie_id = Column(Integer, ForeignKey(''))
    rating = Column(Integer)


class done_projects(Base):
    __tablename__ = 'interviews'
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