from sqlalchemy import Column, String, Integer, ForeignKey

from database.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    i = Column(String)
    d = Column(String)

class Signature(Base):
    __tablename__ = 'signature'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user.id'))
    document = Column(String)