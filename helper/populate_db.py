import csv
import logging
import os
from datetime import datetime, date, time, timedelta
from dateutil import tz

from dbschema.models import (Users, UserInterventionState, DialogQuestions, DialogOpenAnswers, DialogClosedAnswers,
                             FirstAidKit, InterventionActivity, InterventionComponents, InterventionPhases,
                             UserPreferences, InterventionActivitiesPerformed, ClosedAnswers)
from helper.helper_functions import get_db_session
from helper.definitions import (Phases, PreparationInterventionComponents, PreparationInterventionComponentsTriggers,
                                ExecutionInterventionComponents, ExecutionInterventionComponentsTriggers,
                                DialogQuestionsEnum)


tz_nl = tz.gettz("Europe/Amsterdam")


def populate_db_with_test_data(session, test_user_id, activities_file_path='../utils/activities.csv'):
    """
    Populate the database with test data. Update data if it already exists.
    """
    # Fill question table
    objects_questions = initialize_questions()
    [session.merge(obj) for obj in objects_questions]

    # Fill closed answers table
    objects_closed_answers = initialize_closed_anwers()
    [session.merge(obj) for obj in objects_closed_answers]
    
    # Fill in intervention activities (placeholder activities for now)
    objects_intervention_activities = initialize_activities(activities_file_path)
    [session.merge(obj) for obj in objects_intervention_activities]

    objects_preparation_components = initialize_preparation_components_table()
    [session.merge(obj) for obj in objects_preparation_components]

    objects_execution_components = initialize_execution_components_table()
    [session.merge(obj) for obj in objects_execution_components]

    objects_phases = initialize_phases_table()
    [session.merge(obj) for obj in objects_phases]

    objects = create_test_data(test_user_id)
    [session.merge(obj) for obj in objects]

    session.commit()


def initialize_questions():
    data = [
        DialogQuestions(question_id=DialogQuestionsEnum.FUTURE_SELF_SMOKER_WORDS.value,
                        question_description='future self dialog - smoker words'),
        DialogQuestions(question_id=DialogQuestionsEnum.FUTURE_SELF_SMOKER_WHY.value,
                        question_description='future self dialog - smoker why'),
        DialogQuestions(question_id=DialogQuestionsEnum.FUTURE_SELF_MOVER_WORDS.value,
                        question_description='future self dialog - mover words'),
        DialogQuestions(question_id=DialogQuestionsEnum.FUTURE_SELF_MOVER_WHY.value,
                        question_description='future self dialog - mover why'),
        DialogQuestions(question_id=DialogQuestionsEnum.FUTURE_SELF_I_SEE_MYSELF_AS_SMOKER.value,
                        question_description='future self dialog - smoker identity'),
        DialogQuestions(question_id=DialogQuestionsEnum.FUTURE_SELF_I_SEE_MYSELF_AS_MOVER.value,
                        question_description='future self dialog - mover identity'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_CRAVING_WHAT_DOING.value,
                        question_description='relapse dialog - craving - what doing'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_CRAVING_HOW_FEEL.value,
                        question_description='relapse dialog - craving - how feel'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_CRAVING_WITH_WHOM.value,
                        question_description='relapse dialog - craving - with whom'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_CRAVING_HAPPENED_SPECIAL.value,
                        question_description='relapse dialog - craving - happened special'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_TYPE_SMOKE.value,
                        question_description='relapse dialog - smoke lapse - type cigarettes'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_NUMBER_CIGARETTES.value,
                        question_description='relapse dialog - smoke lapse - number cigarettes'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_WHAT_DOING.value,
                        question_description='relapse dialog - smoke lapse - what doing'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_HOW_FEEL.value,
                        question_description='relapse dialog - smoke lapse - how feel'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_WITH_WHOM.value,
                        question_description='relapse dialog - smoke lapse - with whom'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_HAPPENED_SPECIAL.value,
                        question_description='relapse dialog - smoke lapse - happened special'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_TYPE_SMOKE.value,
                        question_description='relapse dialog - smoke relapse - type cigarettes'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_NUMBER_CIGARETTES.value,
                        question_description='relapse dialog - smoke relapse - number cigarettes'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_WHAT_DOING.value,
                        question_description='relapse dialog - smoke relapse - what doing'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_HOW_FEEL.value,
                        question_description='relapse dialog - smoke relapse - how feel'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_WITH_WHOM.value,
                        question_description='relapse dialog - smoke relapse - with whom'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_HAPPENED_SPECIAL.value,
                        question_description='relapse dialog - smoke relapse - happened special'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_SPECIFY_PA.value,
                        question_description='relapse dialog - pa - specify pa'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_TYPE.value,
                        question_description='relapse dialog - pa - type'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_TOGETHER.value,
                        question_description='relapse dialog - pa - together'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_WHY_FAIL.value,
                        question_description='relapse dialog - pa - why fail'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_DOING_TODAY.value,
                        question_description='relapse dialog - pa - doing today'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_HAPPENED_SPECIAL.value,
                        question_description='relapse dialog - pa - happened special'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_PA_REFLECT_BARCHART.value,
                        question_description='relapse dialog - pa - reflect on barchart'),
    ]

    return data


def initialize_closed_anwers():
    answer_descriptions = {}
    answer_descriptions[DialogQuestionsEnum.RELAPSE_CRAVING_WHAT_DOING.value] = ['Aan het werk',
                                                                                 'Thuis bezig met klusjes of'
                                                                                 ' huishouden',
                                                                                 'Iets voor jezelf (hobby, met iemand'
                                                                                 ' afspreken)',
                                                                                 'Aan het eten of drinken',
                                                                                 'Net alcohol of koffie gedronken',
                                                                                 'Net wakker geworden',
                                                                                 'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_CRAVING_HOW_FEEL.value] = ['Stress', 'Verdrietig', 'Boos',
                                                                               'Verveeld', 'Honger', 'Bang of angstig',
                                                                               'Blij', 'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_CRAVING_WITH_WHOM.value] = ['Met partner', 'Alleen',
                                                                                'Met vrienden of famillie',
                                                                                'Met kenissen', 'Met collega`s',
                                                                                'Met andere rokers']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_TYPE_SMOKE.value] = ['Sigaretten', 'e-sigaretten', 'shags',
                                                                               'iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_WHAT_DOING.value] = ['Aan het werk',
                                                                               'Thuis bezig met klusjes of huishouden',
                                                                               'Iets voor jezelf (hobby, met iemand'
                                                                               ' afspreken)',
                                                                               'Aan het eten of drinken',
                                                                               'Net alcohol of koffie gedronken',
                                                                               'Net wakker geworden',
                                                                               'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_HOW_FEEL.value] = ['Schuldig', 'Vervelend', 'Verdrietig',
                                                                             'Je had het gevoel dat het niet zou lukken'
                                                                             ' om te stoppen met roken',
                                                                             'Opgelucht']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_WITH_WHOM.value] = ['Met partner', 'Alleen',
                                                                              'Met vrienden of famillie',
                                                                              'Met kenissen', 'Met collega`s',
                                                                              'Met andere rokers']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_TYPE_SMOKE.value] = ['Sigaretten', 'e-sigaretten', 'shags',
                                                                                 'iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_WHAT_DOING.value] = ['Aan het werk',
                                                                                 'Thuis bezig met klusjes of'
                                                                                 ' huishouden',
                                                                                 'Iets voor jezelf (hobby, met iemand'
                                                                                 ' afspreken)',
                                                                                 'Aan het eten of drinken',
                                                                                 'Net alcohol of koffie gedronken',
                                                                                 'Net wakker geworden',
                                                                                 'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_HOW_FEEL.value] = ['Schuldig', 'Vervelend', 'Verdrietig',
                                                                               'Je had het gevoel dat het niet zou'
                                                                               ' lukken om te stoppen met roken',
                                                                               'Opgelucht']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_WITH_WHOM.value] = ['Met partner', 'Alleen',
                                                                                'Met vrienden of famillie',
                                                                                'Met kenissen', 'Met collega`s',
                                                                                'Met andere rokers']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_SPECIFY_PA.value] = ['je gepland had om te bewegen, maar dit nu niet lukt',
                                                                            'je merkt dat het bewegen over het algemeen niet zo goed gaat als je zou willen']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_TOGETHER.value] = ['Ja', 'Nee']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_WHY_FAIL.value] = ['Geen zin', 'Moe en geen energie',
                                                                          'Geen tijd', 'Er is iets tussen gekomen',
                                                                          'Ligt aan het weer', 'Ziek of geblesseerd',
                                                                          'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_DOING_TODAY.value] = ['Aan het werk',
                                                                             'Thuis bezig met klusjes of huishouden',
                                                                             'Iets voor jezelf (hobby, met iemand'
                                                                             ' afspreken)',
                                                                             'Al lichamelijk actief geweest',
                                                                             'Iets anders']

    data = [ClosedAnswers(closed_answers_id=q*100+i,
                          question_id=q,
                          answer_value=i,
                          answer_description=a)
            for q in answer_descriptions
            for i, a in enumerate(answer_descriptions[q], start=1)]
    return data


def initialize_activities(activities_file_path):
    with open(activities_file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [InterventionActivity(intervention_activity_id=int(row['activity_id']),
                                     intervention_activity_title=row['activity_title'],
                                     intervention_activity_description=row['activity_description'],
                                     intervention_activity_full_instructions=row['activity_instructions'],
                                     user_input_required=bool(int(row['input_needed']))) for row in csv_reader]

    return data


def initialize_preparation_components_table():
    data = [
        InterventionComponents(intervention_component_name=PreparationInterventionComponents.PROFILE_CREATION.value,
                               intervention_component_trigger=PreparationInterventionComponentsTriggers.PROFILE_CREATION.value),
        InterventionComponents(intervention_component_name=PreparationInterventionComponents.MEDICATION_TALK.value,
                               intervention_component_trigger=PreparationInterventionComponentsTriggers.MEDICATION_TALK.value),
        InterventionComponents(intervention_component_name=PreparationInterventionComponents.COLD_TURKEY.value,
                               intervention_component_trigger=PreparationInterventionComponentsTriggers.COLD_TURKEY.value),
        InterventionComponents(intervention_component_name=PreparationInterventionComponents.PLAN_QUIT_START_DATE.value,
                               intervention_component_trigger=PreparationInterventionComponentsTriggers.PLAN_QUIT_START_DATE.value),
        InterventionComponents(intervention_component_name=PreparationInterventionComponents.FUTURE_SELF.value,
                               intervention_component_trigger=PreparationInterventionComponentsTriggers.FUTURE_SELF.value),
        InterventionComponents(intervention_component_name=PreparationInterventionComponents.GOAL_SETTING.value,
                               intervention_component_trigger=PreparationInterventionComponentsTriggers.GOAL_SETTING.value)
    ]

    return data


def initialize_execution_components_table():
    data = [
        InterventionComponents(intervention_component_name=ExecutionInterventionComponents.EXECUTION_INTRODUCTION.value,
                               intervention_component_trigger=ExecutionInterventionComponentsTriggers.EXECUTION_INTRODUCTION.value),
        InterventionComponents(intervention_component_name=ExecutionInterventionComponents.GENERAL_ACTIVITY.value,
                               intervention_component_trigger=ExecutionInterventionComponentsTriggers.GENERAL_ACTIVITY.value),
        InterventionComponents(intervention_component_name=ExecutionInterventionComponents.WEEKLY_REFLECTION.value,
                               intervention_component_trigger=ExecutionInterventionComponentsTriggers.WEEKLY_REFLECTION.value),
        InterventionComponents(intervention_component_name=ExecutionInterventionComponents.DAILY_REFLECTION.value,
                               intervention_component_trigger=ExecutionInterventionComponentsTriggers.DAILY_REFLECTION.value)
    ]

    return data


def initialize_phases_table():
    data = [
        InterventionPhases(phase_name=Phases.PREPARATION.value),
        InterventionPhases(phase_name=Phases.EXECUTION.value),
        InterventionPhases(phase_name=Phases.LAPSE.value)
    ]

    return data


def create_test_data(user_id: int):
    data = [
        Users(dob=date(2000, 1, 2), firstname='Walter', gender='MALE', lastname='Test',
              location='Eanske', nicedayuid=user_id),

        FirstAidKit(users_nicedayuid=user_id, user_activity_title="Water my plants",
                    user_activity_description="I want to water all the plants in my house and garden.",
                    datetime=datetime.now().astimezone(tz_nl), activity_rating=1),
        FirstAidKit(users_nicedayuid=user_id, user_activity_title="Go for a walk with my dog",
                    user_activity_description="A quick walk up to the yellow house at the corner is enough.",
                    datetime=datetime.now().astimezone(tz_nl), activity_rating=2),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=1, datetime=datetime.now().astimezone(tz_nl), activity_rating=1),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=2, datetime=datetime.now().astimezone(tz_nl), activity_rating=2),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=3, datetime=datetime.now().astimezone(tz_nl), activity_rating=3),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=4, datetime=datetime.now().astimezone(tz_nl), activity_rating=4),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=5, datetime=datetime.now().astimezone(tz_nl), activity_rating=5),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=6, datetime=datetime.now().astimezone(tz_nl), activity_rating=6),
        FirstAidKit(users_nicedayuid=user_id, user_activity_title="Eat carrots",
                    user_activity_description="Eat as many carrots as I can.",
                    datetime=datetime.now().astimezone(tz_nl), activity_rating=3),

        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='Fijn plezierig helpt mij ', question_id=1,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='onderdeel van mijn leven verslavend niet zo heel erg',
                          question_id=1, datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='stressvol straf lastig ', question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='lastig', question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='moet voor mijn gezondheid prettig', question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='moet voor mijn gezondheid goed', question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogClosedAnswers(users_nicedayuid=user_id, closed_answers_id=803, datetime=datetime.now().astimezone(tz_nl)),
        DialogClosedAnswers(users_nicedayuid=user_id, closed_answers_id=1401, datetime=datetime.now().astimezone(tz_nl)),
        UserInterventionState(users_nicedayuid=user_id, intervention_phase_id=1, intervention_component_id=5,
                              completed=False, last_time=datetime.now().astimezone(tz_nl), last_part=1),

        UserPreferences(users_nicedayuid=user_id, intervention_component_id=5,
                        recursive=True, week_days='1,2,3,4,5,6,7',
                        preferred_time=(datetime.now().astimezone(tz_nl)+timedelta(minutes=3))),
        UserPreferences(users_nicedayuid=user_id, intervention_component_id=7,
                        recursive=True, week_days='1,2,3,4,5,6,7',
                        preferred_time=(datetime.now().astimezone(tz_nl)+timedelta(minutes=4))),
        UserPreferences(users_nicedayuid=user_id, intervention_component_id=8,
                        recursive=True, week_days='1,2,3,4,5,6,7',
                        preferred_time=(datetime.now().astimezone(tz_nl)+timedelta(minutes=5))),
        UserPreferences(users_nicedayuid=user_id, intervention_component_id=9,
                        recursive=True, week_days='1,2,3,4,5,6,7',
                        preferred_time=(datetime.now().astimezone(tz_nl)+timedelta(minutes=6))),
        UserPreferences(users_nicedayuid=user_id, intervention_component_id=10,
                        recursive=True, week_days='1,2,3,4,5,6,7',
                        preferred_time=(datetime.now().astimezone(tz_nl)+timedelta(minutes=7))),

        InterventionActivitiesPerformed(users_nicedayuid=user_id, intervention_activity_id=1)
    ]

    return data


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    # Heroku and docker-compose will provide the db url as environment variable. If this variable
    # cant be found, the defaults from the helper module will be used.
    try:
        db_url = os.environ['DATABASE_URL']
        test_user_id = os.environ['TEST_USER_ID']
        session = get_db_session(db_url)
    except KeyError:
        session = get_db_session()

    populate_db_with_test_data(session, test_user_id)
    logging.info('Successfully populated database with test data')
