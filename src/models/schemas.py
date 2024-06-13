import datetime
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"
    timestamp: Mapped[datetime] = mapped_column(primary_key=True)
    channel: Mapped[int] = mapped_column(ForeignKey("channel.id"))
    author: Mapped[str]
    message: Mapped[str]

    def __repr__(self):
        return f'({self.timestamp})-[{self.author}]: {self.message} \n'

    def __init__(self, guild: int, channel: int, author: str, message: str):
        self.timestamp = datetime.now()
        self.guild = guild
        self.channel = channel
        self.author = author
        self.message = message

class Guild(Base):
    __tablename__ = "guild"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class GuildChannel(Base):
    __tablename__ = "channel"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    guild_id: Mapped[int] = mapped_column(ForeignKey("guild.id"))

    def __init__(self, id: int, name: str, guild_id: int):
        self.id = id
        self.name = name
        self.guild_id = guild_id


