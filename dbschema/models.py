from sqlalchemy import Column, Date, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    closed_user_answers = relationship('ClosedUserAnswers')
    firstname = Column(String)
    lastname = Column(String)
    location = Column(String)
    gender = Column(String)
    dob = Column(Date)


class ClosedUserAnswers(Base):
    __tablename__ = 'closed_user_answers'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    value = Column(Integer)
    question = Column(String)
    datetime = Column(DateTime)
