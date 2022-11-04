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
    __tablename__ = 'requests'
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