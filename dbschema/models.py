from sqlalchemy import Column, Date, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    nicedayuid = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    location = Column(String)
    gender = Column(String)
    dob = Column(Date)

    # Refer to children tables
    closed_user_answers = relationship('ClosedUserAnswers')
    future_self_dialog_answers = relationship('FutureSelfDialogAnswers', backeref="users", uselist=False)


class ClosedUserAnswers(Base):
    __tablename__ = 'closed_user_answers'
    id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    value = Column(Integer)
    question = Column(String)
    datetime = Column(DateTime)


class FutureSelfDialogAnswers(Base):
    __tablename__ = 'future_self_dialog_answers'
    nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'), primary_key=True)
    smoker_words = Column(String)
    why_smoker_words = Column(String)
    mover_words = Column(String)
    why_mover_words = Column(String)
