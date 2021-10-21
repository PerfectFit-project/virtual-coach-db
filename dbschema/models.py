from sqlalchemy import Column, Date, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    closed_user_answers = relationship('Closed_user_answers')
    nicedayuid = Column(Integer)
    firstname = Column(String)
    lastname = Column(String)
    location = Column(String)
    gender = Column(String)
    dob = Column(Date)


class Closed_user_answers(Base):
    __tablename__ = 'closed_user_answers'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    # parent = relationship("Users", back_populates="closed_user_answers")
    value = Column(Integer)
    question = Column(String)
    datetime = Column(DateTime)
