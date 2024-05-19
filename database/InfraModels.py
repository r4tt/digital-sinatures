from sqlalchemy import Column, String

from database.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    i = Column(String)
    d = Column(String)