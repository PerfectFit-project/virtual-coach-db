from sqlalchemy import (Column, Date, ForeignKey, Integer,
                        String, Boolean, TIMESTAMP, DateTime, func)
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
    dialog_closed_answers = relationship('DialogClosedAnswers')
    dialog_open_answers = relationship('DialogOpenAnswers')
    user_intervention_state = relationship("UserInterventionState", back_populates="user")
    user_preferences = relationship("UserPreferences", back_populates="user")
    first_aid_kit = relationship("FirstAidKit", back_populates="user")
    intervention_activities_performed = relationship("InterventionActivitiesPerformed", back_populates="user")


class DialogClosedAnswers(Base):
    __tablename__ = 'dialog_closed_answers'
    dialog_closed_answers_id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    closed_answers_id = Column(Integer, ForeignKey('closed_answers.closed_answers_id'))
    datetime = Column(TIMESTAMP(timezone=True), default=func.now())

    # Refer relationship
    closed_answers = relationship('ClosedAnswers')


class DialogOpenAnswers(Base):
    __tablename__ = 'dialog_open_answers'
    dialog_open_answers_id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    question_id = Column(Integer, ForeignKey('dialog_questions.question_id'))
    answer_value = Column(String)
    datetime = Column(TIMESTAMP(timezone=True), default=func.now())

    # Refer relationship
    dialog_questions = relationship("DialogQuestions", back_populates="dialog_open_answers")


class ClosedAnswers(Base):
    __tablename__ = 'closed_answers'
    closed_answers_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('dialog_questions.question_id'))
    answer_value = Column(Integer)
    answer_description = Column(String)

    # Refer relationship
    dialog_questions = relationship("DialogQuestions", back_populates="closed_answers")


class DialogQuestions(Base):
    __tablename__ = 'dialog_questions'
    question_id = Column(Integer, primary_key=True)
    question_description = Column(String)

    # Refer relationships
    dialog_open_answers = relationship("DialogOpenAnswers", back_populates="dialog_questions")
    closed_answers = relationship("ClosedAnswers", back_populates="dialog_questions")


class FirstAidKit(Base):
    __tablename__ = "first_aid_kit"
    first_aid_kit_id = Column(Integer, primary_key=True, autoincrement=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))

    # We either provide the ID of one of our own activities, or we store an activity title and description as provided by a user.
    intervention_activity_id = Column(Integer, ForeignKey('intervention_activity.intervention_activity_id'))
    user_activity_title = Column(String(100))
    user_activity_description = Column(String)
    activity_rating = Column(Integer)

    datetime = Column(TIMESTAMP(timezone=True), default=func.now())

    # Refer to relationships
    user = relationship("Users", back_populates="first_aid_kit")
    intervention_activity = relationship("InterventionActivity")


class InterventionActivity(Base):
    __tablename__ = 'intervention_activity'
    intervention_activity_id = Column(Integer, primary_key=True)
    intervention_activity_title = Column(String(100))
    intervention_activity_description = Column(String)
    intervention_activity_full_instructions = Column(String)
    user_input_required = Column(Boolean)


class InterventionActivitiesPerformed(Base):
    __tablename__ = 'intervention_activities_performed'
    intervention_activities_performed_id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    intervention_activity_id = Column(Integer, ForeignKey('intervention_activity.intervention_activity_id'))
    completed_datetime = Column(DateTime(timezone=True),
                                default=func.now())
    user_input = Column(String)

    user = relationship("Users", back_populates="intervention_activities_performed")
    intervention_activity = relationship("InterventionActivity")

class InterventionPhases(Base):
    __tablename__ = 'intervention_phases'
    phase_id = Column(Integer, primary_key=True, autoincrement=True)
    phase_name = Column(String(100))


class InterventionComponents(Base):
    __tablename__ = 'intervention_components'
    intervention_component_id = Column(Integer, primary_key=True, autoincrement=True)
    intervention_component_name = Column(String(100))
    intervention_component_trigger = Column(String(100))


class UserInterventionState(Base):
    __tablename__ = 'user_intervention_state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    intervention_phase_id = Column(Integer, ForeignKey('intervention_phases.phase_id'))
    intervention_component_id = Column(Integer, ForeignKey('intervention_components.intervention_component_id'))
    completed = Column(Boolean)
    last_time = Column(TIMESTAMP(timezone=True), default=func.now())
    last_part = Column(Integer)
    next_planned_date = Column(DateTime(timezone=True), nullable=True)
    task_uuid = Column(String(36), nullable=True)

    user = relationship("Users", back_populates="user_intervention_state")
    phase = relationship("InterventionPhases")
    intervention_component = relationship("InterventionComponents")


class UserPreferences(Base):
    __tablename__ = 'user_preferences'
    user_preferences_id = Column(Integer, primary_key=True, autoincrement=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    intervention_component_id = Column(Integer, ForeignKey('intervention_components.intervention_component_id'))
    recursive = Column(Boolean)
    week_days = Column(String(13))
    preferred_time = Column(TIMESTAMP(timezone=True))

    user = relationship("Users", back_populates="user_preferences")
    intervention_component = relationship("InterventionComponents")
