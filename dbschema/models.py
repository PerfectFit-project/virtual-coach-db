from sqlalchemy import (Column, Date, ForeignKey, Integer, Float,
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
    participant_code = Column(String(5))
    
    # For goal-setting dialog testimonial choice
    testim_godin_activity_level = Column(Integer)  # Goding leisure-time activity level (0, 1, 2)
    testim_running_walking_pref = Column(Integer)  # 0 if people prefer walking and 1 if people prefer running
    testim_self_efficacy_pref = Column(Float)  # Self-efficacy for preferred activity (i.e., running or walking), ranges from 0 to 100.
    testim_sim_cluster_1 = Column(Float)  # Perceived similarity to people in cluster 1 based on 2 prototypes, ranges from -3 to 3
    testim_sim_cluster_3 = Column(Float)  # Perceived similarity to people in cluster 3 based on 2 prototypes, ranges from -3 to 3

    # For goal-setting dialog, quit date and long-term goal pa
    quit_date = Column(Date)
    long_term_pa_goal = Column(String)

    # For final evaluation
    pf_evaluation_grade = Column(Integer)
    pf_evaluation_comment = Column(String)
    
    # Timing preferences for intervention
    week_days = Column(String(13))
    preferred_time = Column(TIMESTAMP(timezone=True))
    
    # Refer to relationships
    dialog_closed_answers = relationship('DialogClosedAnswers')
    dialog_open_answers = relationship('DialogOpenAnswers')
    user_intervention_state = relationship("UserInterventionState", back_populates="user")
    user_preferences = relationship("UserPreferences", back_populates="user")
    first_aid_kit = relationship("FirstAidKit", back_populates="user")
    intervention_activities_performed = relationship("InterventionActivitiesPerformed", back_populates="user")
    step_counts = relationship("StepCounts", back_populates="user")
    
    
class Testimonials(Base):
    __tablename__ = "testimonials"
    testimonial_id = Column(Integer, primary_key=True)
    godin_activity_level = Column(Integer)
    running_walking_pref = Column(Integer)  # Whether the goal is a walking (0) or a running goal (1)
    self_efficacy_pref = Column(Float)
    testimonial_text = Column(String)
    part_of_cluster1 = Column(Boolean)
    part_of_cluster3 = Column(Boolean)

class StepCounts(Base):
    __tablename__ = "step_counts"
    step_count_id = Column(Integer, primary_key=True)
    users_nicedayuid = Column(Integer, ForeignKey('users.nicedayuid'))
    value = Column(Integer)
    datetime = Column(TIMESTAMP(timezone=True), default=func.now())

    user = relationship("Users", back_populates="step_counts")

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

    # Each activity in first aid kit is one of our intervention activities
    intervention_activity_id = Column(Integer, ForeignKey('intervention_activity.intervention_activity_id'))
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
    intervention_activity_benefit = Column(String)


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

