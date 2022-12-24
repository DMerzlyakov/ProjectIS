from sqlalchemy import create_engine

from src.config.config import DATABASE_URL
from src.data.entity.models import Base

if __name__ == '__main__':
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
