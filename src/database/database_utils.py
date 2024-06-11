from typing import Type

from sqlalchemy import Engine
from sqlalchemy.engine.create import event
from sqlalchemy.orm import sessionmaker

from src.database.db_setup import engine
from src.models.schemas import Base

Session = sessionmaker(bind=engine)
db = Session()



@event.listens_for(Engine, "connect")
def enable_sqlite_fks(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

def add(db_model: Base) -> None:
    # Errorhandling needs to be done
    db.add(db_model)
    db.commit()
    db.refresh(db_model)  # i dont know what this does


def delete(table: Type[Base], id: str) -> None:
    result: Base | None = db.get(table, id)
    db.delete(result)
    db.commit()


def get_all(table: Type[Base]) -> list[Base]:
    # how to query SELECT *
    results: list[Base] = db.query(table).all()
    return results
