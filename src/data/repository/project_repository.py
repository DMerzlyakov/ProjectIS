from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.config.config import *


def connect_db():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())
    return session
