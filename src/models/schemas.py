import datetime
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"
    timestamp: Mapped[datetime] = mapped_column(primary_key=True)
    guild: Mapped[str]
    channel: Mapped[str]
    author: Mapped[str]
    message: Mapped[str]

    def __repr__(self):
        return f'({self.timestamp})-{self.guild}-{self.channel}-[{self.author}]-{self.message} \n'

    def __init__(self, guild: str, channel: str, author: str, message: str):
        self.timestamp = datetime.now()
        self.guild = guild
        self.channel = channel
        self.author = author
        self.message = message

class Guild(Base):
    __tablename__ = "guild"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class GuildChannel(Base):
    __tablename__ = "channel"
    id: Mapped[id] = mapped_column(primary_key=True)
    name: Mapped[str]
    guild_id: Mapped[int] = mapped_column(ForeignKey("guild.id"))

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

