from datetime import datetime
from dateutil import tz
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, TIMESTAMP
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

    # Refer to relationships
    dialog_answers = relationship('DialogAnswers')
    user_intervention_state = relationship("UserInterventionState", back_populates="user")


class DialogAnswers(Base):
    __tablename__ = 'dialog_answers'
    answer_id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    answer = Column(String)
    question_id = Column(Integer, ForeignKey('dialog_questions.question_id'))
    datetime = Column(TIMESTAMP(timezone=True), default = datetime.now().astimezone(tz.gettz("Europe/Amsterdam")))

    # Refer relationship
    dialog_questions = relationship('DialogQuestions')


class DialogQuestions(Base):
    __tablename__ = 'dialog_questions'
    question_id = Column(Integer, primary_key=True)
    question_description = Column(String)


class UserInterventionState(Base):
    __tablename__ = 'user_intervention_state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    intervention_component = Column(String)             
    last_time = Column(TIMESTAMP(timezone=True), default = datetime.now().astimezone(tz.gettz("Europe/Amsterdam")))
    last_part = Column(Integer)
    user = relationship("Users", back_populates="user_intervention_state")
