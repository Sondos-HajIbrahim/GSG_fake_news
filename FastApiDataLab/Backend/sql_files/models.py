from sqlalchemy import Boolean, Column, Integer, String, Boolean, Enum

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String)
    hashed_password = Column(String)


class News(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    added_by = Column(Enum('system', 'admin'))
    fake = Column(Boolean)
