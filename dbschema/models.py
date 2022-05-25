from datetime import datetime
from dateutil import tz
from sqlalchemy import Column, Date, ForeignKey, Integer, String, TIMESTAMP
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
    closed_user_answers = relationship('ClosedUserAnswers')
    dialog_answers = relationship('DialogAnswers')
    user_intervention_state = relationship("UserInterventionState", back_populates="user")
    first_aid_kit = relationship("FirstAidKit", back_populates="user")


class ClosedUserAnswers(Base):
    __tablename__ = 'closed_user_answers'
    id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    value = Column(Integer)
    question = Column(String)
    datetime = Column(TIMESTAMP(timezone=True), default = datetime.now().astimezone(tz.gettz("Europe/Amsterdam")))


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

 
class FirstAidKit(Base):
    __tablename__ = "first_aid_kit"
    first_aid_kit_id = Column(Integer, primary_key=True, autoincrement=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    
    # We either provide the ID of one of our own activities, or we store an activity title and description as provided by a user.
    intervention_activity_id = Column(Integer, ForeignKey('intervention_activity.intervention_activity_id'))
    user_activity_title = Column(String(100))
    user_activity_description = Column(String)
    
    datetime = Column(TIMESTAMP(timezone=True), default = datetime.now().astimezone(tz.gettz("Europe/Amsterdam")))
    
    # Refer to relationships
    user = relationship("Users", back_populates="first_aid_kit")
    intervention_activity = relationship("InterventionActivity")
    
    
class InterventionActivity(Base):
    __tablename__ = 'intervention_activity'
    intervention_activity_id = Column(Integer, primary_key=True)
    intervention_activity_title = Column(String(100))
    intervention_activity_description = Column(String)
    intervention_activity_full_instructions = Column(String)


class UserInterventionState(Base):
    __tablename__ = 'user_intervention_state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    intervention_component = Column(String)             
    last_time = Column(TIMESTAMP(timezone=True), default = datetime.now().astimezone(tz.gettz("Europe/Amsterdam")))
    last_part = Column(Integer)
    user = relationship("Users", back_populates="user_intervention_state")
