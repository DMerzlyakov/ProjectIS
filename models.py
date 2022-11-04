from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Boolean, create_engine
from sqlalchemy.orm import declarative_base, relationship
import psycopg2

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
    role_id = Column(Integer, ForeignKey(''))
    skill_id = Column(Integer, ForeignKey(''))
    firstName = Column(String)
    lastName = Column(String)
    secondName = Column(String)
    vacancy_id = Column(Integer, ForeignKey(''))


class EmployeesSkills(Base):
    __tablename__ = 'employeesSkills'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill_id = Column(Integer, ForeignKey(''))
    employee_id = Column(Integer, ForeignKey(''))


class EmployeesRole(Base):
    __tablename__ = 'employeesRole'
    __table_args__ = {
        'schema': 'public',
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey(''))
    employee_id = Column(Integer, ForeignKey(''))
