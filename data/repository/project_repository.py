from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    session = Session(bind=engine.connect())
    return session