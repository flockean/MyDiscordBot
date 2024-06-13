import logging
import os
from sqlalchemy import create_engine

from sqlalchemy.orm import Session
from src.models.schemas import Base

db_path: str = '/src/volume/discordFiles.db'
engine = create_engine(f'sqlite://{db_path}', connect_args={"check_same_thread": False})


# with sqlalchemy you are able to store python objects in a database,
# therefore you first need to create some python classes

# create db shiat
def init_db() -> None:
    if not os.path.exists(f'.{db_path}'):
        logging.info("Creating database")
        Base.metadata.create_all(bind=engine)
        with Session(engine) as session:
            session.commit()
