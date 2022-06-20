import logging
import os
from datetime import datetime, date
from dateutil import tz

from dbschema.models import Users, ClosedUserAnswers, UserInterventionState, DialogQuestions, DialogAnswers, FirstAidKit, InterventionActivity, InterventionComponents, InterventionPhases
from helper import get_db_session
from definitions import Phases, PreparationDialogs

def populate_db_with_test_data(session):
    """
    Populate the database with test data. Update data if it already exists.
    """
    # Fill question table
    objects_questions = [
        DialogQuestions(question_id=1, question_description='future self dialog - smoker words'),
        DialogQuestions(question_id=2, question_description='future self dialog - smoker why'),
        DialogQuestions(question_id=3, question_description='future self dialog - mover words'),
        DialogQuestions(question_id=4, question_description='future self dialog - mover why'),
        DialogQuestions(question_id=5, question_description='future self dialog - smoker identity'),
        DialogQuestions(question_id=6, question_description='future self dialog - mover identity')
    ]
    [session.merge(obj) for obj in objects_questions]
    
    
    # Fill in intervention activities (placeholder activities for now)
    objects_intervention_activities = [
        InterventionActivity(intervention_activity_id=1, 
                             intervention_activity_title="Relaxation exercise", 
                             intervention_activity_description="Go to this link to listen to the instructions for the relaxation exercise: ... .",
                             intervention_activity_full_instructions='Now here are very detailed instructions for the relaxation exercise.'),
        InterventionActivity(intervention_activity_id=2, 
                             intervention_activity_title="Reasons to quit", 
                             intervention_activity_description="Think back about the reasons why you want to quit smoking.",
                             intervention_activity_full_instructions="These are very detailed instructions for reasons for quitting."),
        InterventionActivity(intervention_activity_id=3, 
                             intervention_activity_title="Reasons to be physically active", 
                             intervention_activity_description="Think again about why you want to be physically active. Maybe you still have the list on your fridge.",
                             intervention_activity_full_instructions="Now here are very detailed step-by-step instructions on reasons for PA.")    
    ]
    [session.merge(obj) for obj in objects_intervention_activities]

    objects_intervention_components = initialize_intervention_components_table()
    [session.merge(obj) for obj in objects_intervention_components]

    objects_phases = initialize_phases_table()
    [session.merge(obj) for obj in objects_phases]

    tz_nl = tz.gettz("Europe/Amsterdam")

    objects = [
        Users(dob=date(2019, 4, 13), firstname='Sven', gender='MALE', lastname='van der burg',
              location='Damsko', nicedayuid=38527),
        Users(dob=date(2018, 1, 2), firstname='Nele', gender='FEMALE', lastname='Albers',
              location='Delft', nicedayuid=40121),
        Users(dob=date(2000, 1, 2), firstname='Bouke', gender='MALE', lastname='RRD',
              location='Eanske', nicedayuid=41215),
        Users(dob=date(2000, 1, 2), firstname='User', gender='MALE', lastname='Test',
              location='Eanske', nicedayuid=41538),
        ClosedUserAnswers(users_nicedayuid=38527, value=3, question='paevaluation', datetime=datetime.now().astimezone(tz_nl)),
        ClosedUserAnswers(users_nicedayuid=38527, value=5, question='paevaluation', datetime=datetime.now().astimezone(tz_nl)),
        ClosedUserAnswers(users_nicedayuid=38527, value=4, question='paevaluation', datetime=datetime.now().astimezone(tz_nl)),
        ClosedUserAnswers(users_nicedayuid=40121, value=2, question='paevaluation', datetime=datetime.now().astimezone(tz_nl)),
        ClosedUserAnswers(users_nicedayuid=40121, value=1, question='paevaluation', datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=40121, user_activity_title="Water my plants", 
                    user_activity_description="I want to water all the plants in my house and garden.", 
                    datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=40121, user_activity_title="Go for a walk with my dog", 
                    user_activity_description="A quick walk up to the yellow house at the corner is enough.",
                    datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=40121, intervention_activity_id=1, datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=38527, intervention_activity_id=1, datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=41538, intervention_activity_id=2, datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=41538, intervention_activity_id=3, datetime=datetime.now().astimezone(tz_nl)),
        FirstAidKit(users_nicedayuid=41538, user_activity_title="Eat carrots", 
                    user_activity_description="Eat as many carrots as I can.", 
                    datetime=datetime.now().astimezone(tz_nl)),
        DialogAnswers(users_nicedayuid=38527, answer='lekker stoer eng', question_id=1,
                      datetime=datetime.now().astimezone(tz_nl)),
        DialogAnswers(users_nicedayuid=40121, answer='lekker leuk eng', question_id=1,
                      datetime=datetime.now().astimezone(tz_nl)),
        DialogAnswers(users_nicedayuid=40121, answer='eng leuk stoer', question_id=3,
                      datetime=datetime.now().astimezone(tz_nl)),
        UserInterventionState(users_nicedayuid=40121, intervention_phase_id=1, intervention_component_id=1, completed=False, last_time=datetime.now().astimezone(tz_nl), last_part=1)
    ]
    [session.merge(obj) for obj in objects]

    session.commit()


def initialize_intervention_components_table():
    data = [
        InterventionComponents(intervention_component_name=PreparationDialogs.PROFILE_CREATION.value),
        InterventionComponents(intervention_component_name=PreparationDialogs.MEDICATION_TALK.value),
        InterventionComponents(intervention_component_name=PreparationDialogs.COLD_TURKEY.value),
        InterventionComponents(intervention_component_name=PreparationDialogs.PLAN_QUIT_START_DATE.value),
        InterventionComponents(intervention_component_name=PreparationDialogs.FUTURE_SELF.value),
        InterventionComponents(intervention_component_name=PreparationDialogs.GOAL_SETTING.value)
    ]

    return data


def initialize_phases_table():
    data = [
        InterventionPhases(phase_name=Phases.PREPARATION.value),
        InterventionPhases(phase_name=Phases.EXECUTION.value),
        InterventionPhases(phase_name=Phases.LAPSE.value)
    ]

    return data


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    # Heroku and docker-compose will provide the db url as environment variable. If this variable
    # cant be found, the defaults from the helper module will be used.
    try:
        db_url = os.environ['DATABASE_URL']
        session = get_db_session(db_url)
    except KeyError:
        session = get_db_session()

    populate_db_with_test_data(session)
    logging.info('Succesfully populated database with test data')
