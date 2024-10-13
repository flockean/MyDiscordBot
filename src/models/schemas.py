import datetime
from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class DMMessage(Base):
    __tablename__ = "dmmessage"
    id: Mapped[datetime] = mapped_column(primary_key=True)
    author: Mapped[str]
    content: Mapped[str]

    def __init__(self, author, content):
        self.id = datetime.now()
        self.author = author
        self.content = content

    def __repr__(self):
        return f'{self.id} - {self.author} - {self.content} \n'

class GameProgress(Base):
    __tablename__ = "game_progress"
    id_name: Mapped[str] = mapped_column(primary_key=True)
    game_type: Mapped[str] = mapped_column(ForeignKey("game_type.id_name"))
    in_progress: Mapped[int]

    game_category: Mapped["GameType"] = relationship(back_populates="game_progress", primaryjoin="GameProgress.game_type==GameType.id_name")

    def __init__(self, id_name, game_type, in_progress):
        self.id_name = id_name
        self.game_type = game_type
        self.in_progress = in_progress

    def __repr__(self):
        return f'> {self.in_progress} {self.id_name}'


class GameType(Base):
    __tablename__ = "game_type"
    id_name: Mapped[str] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"{self.id_name}"

class ProgressStatus(Enum):
    notStarted = 1
    inProgress = 2
    finished = 3

