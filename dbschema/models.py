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
    dialog_answers = relationship('DialogAnswers')


class ClosedUserAnswers(Base):
    __tablename__ = 'closed_user_answers'
    id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    value = Column(Integer)
    question = Column(String)
    datetime = Column(DateTime)


class DialogAnswers(Base):
    __tablename__ = 'dialog_answers'
    answer_id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    answer = Column(String)
    question_id = Column(Integer, ForeignKey('dialog_questions.question_id'))
    datetime = Column(DateTime)
    dialog_questions = relationship('DialogQuestions')


class DialogQuestions(Base):
    __tablename__ = 'dialog_questions'
    question_id = Column(Integer, primary_key=True)
    question_description = Column(String)
