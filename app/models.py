import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP

from .database import Base


class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now)
