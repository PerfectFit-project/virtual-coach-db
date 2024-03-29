import csv
import logging
import os

from typing import Any
from dbschema.models import (DialogQuestions, InterventionActivity, InterventionComponents,
                             InterventionPhases, ClosedAnswers, Testimonials)
from helper.helper_functions import get_db_session
from helper.definitions import (Phases, Components, ComponentsTriggers,
                                DialogQuestionsEnum, Notifications, NotificationsTriggers)


def populate_db_fixed_data(session,
                           activities_file_path='../utils/activities.csv',
                           testimonials_file_path='../utils/testimonials_with_user_data.csv'):
    """
    Populate the database with the fixed needed data, after checking that they do not exist already.
    """
    # Fill question table
    if is_table_empty(session, DialogQuestions):
        objects_questions = initialize_questions()
        [session.merge(obj) for obj in objects_questions]

    # Fill closed answers table
    if is_table_empty(session, ClosedAnswers):
        objects_closed_answers = initialize_closed_answers()
        [session.merge(obj) for obj in objects_closed_answers]

    # Fill in intervention activities
    if is_table_empty(session, InterventionActivity):
        objects_intervention_activities = initialize_activities(activities_file_path)
        [session.merge(obj) for obj in objects_intervention_activities]

    # Fill in testimonials (to be shown in goal-setting dialog)
    if is_table_empty(session, Testimonials):
        objects_testimonials = initialize_testimonials(testimonials_file_path)
        [session.merge(obj) for obj in objects_testimonials]

    if is_table_empty(session, InterventionComponents):
        objects_preparation_components = initialize_preparation_components_table()
        [session.merge(obj) for obj in objects_preparation_components]

        objects_execution_components = initialize_execution_components_table()
        [session.merge(obj) for obj in objects_execution_components]

        objects_notification_components = initialize_notifications_components_table()
        [session.merge(obj) for obj in objects_notification_components]

    if is_table_empty(session, InterventionPhases):
        objects_phases = initialize_phases_table()
        [session.merge(obj) for obj in objects_phases]

    session.commit()


def is_table_empty(session, table) -> bool:
    """
    Check if a table in the DB is empty or if it contains data.
    Args:
        table: The class of the specific tale to be checked, as defined in models.py

    Returns: True if the table is empty, False otherwise

    """
    entries = (session.query(table).count())

    if entries > 0:
        return False

    return True


# dialog_questions table
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
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_CRAVING_REFLECT_BARCHART.value,
                        question_description='relapse dialog - craving - reflect on barchart'),
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
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_LAPSE_REFLECT_BARCHART.value,
                        question_description='relapse dialog - smoke lapse - reflect on barchart'),
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
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_RELAPSE_REFLECT_BARCHART.value,
                        question_description='relapse dialog - smoke relapse - reflect on barchart'),
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
        DialogQuestions(question_id=DialogQuestionsEnum.PERSUASION_PROMPTS.value,
                        question_description='persuasion - activity - prompts'),
        DialogQuestions(question_id=DialogQuestionsEnum.PERSUASION_WANT.value,
                        question_description='persuasion - activity - want'),
        DialogQuestions(question_id=DialogQuestionsEnum.PERSUASION_NEED.value,
                        question_description='persuasion - activity - need'),
        DialogQuestions(question_id=DialogQuestionsEnum.PERSUASION_EFFORT.value,
                        question_description='persuasion - activity - effort'),
        DialogQuestions(question_id=DialogQuestionsEnum.PERSUASION_TYPE.value,
                        question_description='persuasion - activity - chosen persuasion type'),
        DialogQuestions(question_id=DialogQuestionsEnum.PERSUASION_MESSAGE_INDEX.value,
                        question_description='persuasion - activity - persuasive message index'),
        DialogQuestions(question_id=DialogQuestionsEnum.RELAPSE_SMOKE_HRS_LAPSE_RELAPSE.value,
                        question_description='hrs - lapse - relapse branch in relapse dialog')
    ]

    return data


# closed_answers table
def initialize_closed_answers():
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
    answer_descriptions[DialogQuestionsEnum.RELAPSE_CRAVING_HOW_FEEL.value] = ['Stress', 'Moe',
                                                                               'Verdrietig', 'Boos',
                                                                               'Verveeld', 'Honger',
                                                                               'Bang of angstig',
                                                                               'Blij',
                                                                               'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_CRAVING_WITH_WHOM.value] = ['Met partner',
                                                                                'Alleen',
                                                                                'Met vrienden of famillie',
                                                                                'Met kenissen',
                                                                                'Met collega`s',
                                                                                'Met andere rokers']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_TYPE_SMOKE.value] = ['Sigaretten',
                                                                               'e-sigaretten',
                                                                               'shags',
                                                                               'iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_WHAT_DOING.value] = ['Aan het werk',
                                                                               'Thuis bezig met klusjes of huishouden',
                                                                               'Iets voor jezelf (hobby, met iemand'
                                                                               ' afspreken)',
                                                                               'Aan het eten of drinken',
                                                                               'Net alcohol of koffie gedronken',
                                                                               'Net wakker geworden',
                                                                               'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_HOW_FEEL.value] = ['Stress',
                                                                             'Moe',
                                                                             'Verdrietig',
                                                                             'Boos',
                                                                             'Verveeld',
                                                                             'Honger',
                                                                             'Bang of angstig',
                                                                             'Blij',
                                                                             'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_LAPSE_WITH_WHOM.value] = ['Met partner',
                                                                              'Alleen',
                                                                              'Met vrienden of famillie',
                                                                              'Met kenissen',
                                                                              'Met collega`s',
                                                                              'Met andere rokers']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_TYPE_SMOKE.value] = ['Sigaretten',
                                                                                 'e-sigaretten',
                                                                                 'shags',
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
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_HOW_FEEL.value] = ['Stress',
                                                                               'Moe',
                                                                               'Verdrietig',
                                                                               'Boos',
                                                                               'Verveeld',
                                                                               'Honger',
                                                                               'Bang of angstig',
                                                                               'Blij',
                                                                               'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_RELAPSE_WITH_WHOM.value] = ['Met partner',
                                                                                'Alleen',
                                                                                'Met vrienden of famillie',
                                                                                'Met kenissen',
                                                                                'Met collega`s',
                                                                                'Met andere rokers']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_SPECIFY_PA.value] = [
        'je gepland had om te bewegen, maar dit nu niet lukt',
        'je merkt dat het bewegen over het algemeen niet zo goed gaat als je zou willen']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_TOGETHER.value] = ['Ja', 'Nee']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_WHY_FAIL.value] = ['Geen zin',
                                                                          'Moe en geen energie',
                                                                          'Geen tijd',
                                                                          'Er is iets tussen gekomen',
                                                                          'Ligt aan het weer',
                                                                          'Ziek of geblesseerd',
                                                                          'Iets anders']
    answer_descriptions[DialogQuestionsEnum.RELAPSE_PA_DOING_TODAY.value] = ['Aan het werk',
                                                                             'Thuis bezig met klusjes of huishouden',
                                                                             'Iets voor jezelf (hobby, met iemand'
                                                                             ' afspreken)',
                                                                             'Je aan het eten of drinken wast',
                                                                             'Je net alcohol of koffie hebt gedronken',
                                                                             'Je net wakker was',
                                                                             'Iets anders']
    answer_descriptions[DialogQuestionsEnum.PERSUASION_PROMPTS.value] = ["Helemaal mee oneens",
                                                                         "Mee oneens",
                                                                         "Niet mee eens, niet mee oneens",
                                                                         "Mee eens",
                                                                         "Helemaal mee eens"]
    answer_descriptions[DialogQuestionsEnum.PERSUASION_WANT.value] = ["Helemaal mee oneens",
                                                                      "Mee oneens",
                                                                      "Niet mee eens, niet mee oneens",
                                                                      "Mee eens",
                                                                      "Helemaal mee eens"]
    answer_descriptions[DialogQuestionsEnum.PERSUASION_NEED.value] = ["Helemaal mee oneens",
                                                                      "Mee oneens",
                                                                      "Niet mee eens, niet mee oneens",
                                                                      "Mee eens",
                                                                      "Helemaal mee eens"]
    answer_descriptions[DialogQuestionsEnum.PERSUASION_EFFORT.value] = ["0", "1", "2", "3", "4",
                                                                        "5",
                                                                        "6", "7", "8", "9", "10"]
    answer_descriptions[DialogQuestionsEnum.PERSUASION_TYPE.value] = ["Commitment",
                                                                      "Consensus",
                                                                      "No persuasion"]
    answer_descriptions[DialogQuestionsEnum.PERSUASION_MESSAGE_INDEX.value] = ["-1", "0", "1", "2",
                                                                               "3", "4", "5"]
    answer_descriptions[DialogQuestionsEnum.RELAPSE_SMOKE_HRS_LAPSE_RELAPSE.value] = ["HRS", "Lapse", "Relapse"]

    data = [ClosedAnswers(closed_answers_id=q * 100 + i,
                          question_id=q,
                          answer_value=i,
                          answer_description=a)
            for q in answer_descriptions
            for i, a in enumerate(answer_descriptions[q], start=1)]
    return data


# intervention_activity table
def initialize_activities(activities_file_path):
    print(activities_file_path)
    with open(activities_file_path, encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [InterventionActivity(intervention_activity_id=int(row['activity_id']),
                                     intervention_activity_title=row['activity_title'],
                                     intervention_activity_description=row['activity_description'],
                                     intervention_activity_full_instructions=row[
                                         'activity_instructions'],
                                     user_input_required=bool(int(row['input_needed'])),
                                     intervention_activity_benefit=row['activity_benefit']) for row
                in csv_reader]

    return data


# testimonials table
def initialize_testimonials(testimonials_file_path):
    with open(testimonials_file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [Testimonials(testimonial_id=int(row['id']),
                             godin_activity_level=int(row['godin_level']),
                             running_walking_pref=int(row['pref_binary']),
                             self_efficacy_pref=float(row['self_efficacy']),
                             part_of_cluster1=bool(int(row["part_of_cluster1"])),
                             part_of_cluster3=bool(int(row["part_of_cluster3"])),
                             testimonial_text=row['testimonial_dutch']) for row in csv_reader]

    return data


# intervention_components table
def initialize_preparation_components_table():
    data = [
        InterventionComponents(
            intervention_component_name=Components.PREPARATION_INTRODUCTION.value,
            intervention_component_trigger=ComponentsTriggers.PREPARATION_INTRODUCTION.value),
        InterventionComponents(intervention_component_name=Components.PROFILE_CREATION.value,
                               intervention_component_trigger=ComponentsTriggers.PROFILE_CREATION.value),
        InterventionComponents(intervention_component_name=Components.MEDICATION_TALK.value,
                               intervention_component_trigger=ComponentsTriggers.MEDICATION_TALK.value),
        InterventionComponents(intervention_component_name=Components.TRACK_BEHAVIOR.value,
                               intervention_component_trigger=ComponentsTriggers.TRACK_BEHAVIOR.value),
        InterventionComponents(intervention_component_name=Components.COLD_TURKEY.value,
                               intervention_component_trigger=ComponentsTriggers.COLD_TURKEY.value),
        InterventionComponents(intervention_component_name=Components.PLAN_QUIT_START_DATE.value,
                               intervention_component_trigger=ComponentsTriggers.PLAN_QUIT_START_DATE.value),
        InterventionComponents(intervention_component_name=Components.FUTURE_SELF_LONG.value,
                               intervention_component_trigger=ComponentsTriggers.FUTURE_SELF_LONG.value),
        InterventionComponents(intervention_component_name=Components.FUTURE_SELF_SHORT.value,
                               intervention_component_trigger=ComponentsTriggers.FUTURE_SELF_SHORT.value),
        InterventionComponents(intervention_component_name=Components.GOAL_SETTING.value,
                               intervention_component_trigger=ComponentsTriggers.GOAL_SETTING.value),
        InterventionComponents(intervention_component_name=Components.FIRST_AID_KIT_VIDEO.value,
                               intervention_component_trigger=ComponentsTriggers.FIRST_AID_KIT_VIDEO.value),
        InterventionComponents(
            intervention_component_name=Components.RESCHEDULING_PREPARATION.value,
            intervention_component_trigger=ComponentsTriggers.RESCHEDULING_PREPARATION.value),
        InterventionComponents(intervention_component_name=Components.WATCH_VIDEO.value,
                               intervention_component_trigger=ComponentsTriggers.WATCH_VIDEO.value),
        InterventionComponents(intervention_component_name=Components.DONE_VIDEO.value,
                               intervention_component_trigger=ComponentsTriggers.DONE_VIDEO.value)
    ]

    return data


# intervention_components table
def initialize_execution_components_table():
    data = [
        InterventionComponents(intervention_component_name=Components.EXECUTION_INTRODUCTION.value,
                               intervention_component_trigger=ComponentsTriggers.EXECUTION_INTRODUCTION.value),
        InterventionComponents(intervention_component_name=Components.GENERAL_ACTIVITY.value,
                               intervention_component_trigger=ComponentsTriggers.GENERAL_ACTIVITY.value),
        InterventionComponents(intervention_component_name=Components.WEEKLY_REFLECTION.value,
                               intervention_component_trigger=ComponentsTriggers.WEEKLY_REFLECTION.value),
        InterventionComponents(intervention_component_name=Components.DAILY_REFLECTION.value,
                               intervention_component_trigger=ComponentsTriggers.DAILY_REFLECTION.value),
        InterventionComponents(intervention_component_name=Components.RELAPSE_DIALOG.value,
                               intervention_component_trigger=ComponentsTriggers.RELAPSE_DIALOG.value),
        InterventionComponents(intervention_component_name=Components.RELAPSE_DIALOG_HRS.value,
                               intervention_component_trigger=ComponentsTriggers.RELAPSE_DIALOG_HRS.value),
        InterventionComponents(intervention_component_name=Components.RELAPSE_DIALOG_LAPSE.value,
                               intervention_component_trigger=ComponentsTriggers.RELAPSE_DIALOG_LAPSE.value),
        InterventionComponents(intervention_component_name=Components.RELAPSE_DIALOG_RELAPSE.value,
                               intervention_component_trigger=ComponentsTriggers.RELAPSE_DIALOG_RELAPSE.value),
        InterventionComponents(intervention_component_name=Components.RELAPSE_DIALOG_PA.value,
                               intervention_component_trigger=ComponentsTriggers.RELAPSE_DIALOG_PA.value),
        InterventionComponents(intervention_component_name=Components.RELAPSE_DIALOG_SYSTEM.value,
                               intervention_component_trigger=ComponentsTriggers.RELAPSE_DIALOG_SYSTEM.value),
        InterventionComponents(intervention_component_name=Components.FIRST_AID_KIT.value,
                               intervention_component_trigger=ComponentsTriggers.FIRST_AID_KIT.value),
        InterventionComponents(intervention_component_name=Components.CLOSING_DIALOG.value,
                               intervention_component_trigger=ComponentsTriggers.CLOSING_DIALOG.value),

        InterventionComponents(
            intervention_component_name=Components.CONTINUE_UNCOMPLETED_DIALOG.value,
            intervention_component_trigger=ComponentsTriggers.CONTINUE_UNCOMPLETED_DIALOG.value),
        InterventionComponents(intervention_component_name=Components.CENTRAL_OPTIONS.value,
                               intervention_component_trigger=ComponentsTriggers.CENTRAL_OPTIONS.value)
    ]

    return data


# intervention_components table
def initialize_notifications_components_table():
    data = [
        InterventionComponents(
            intervention_component_name=Notifications.BEFORE_QUIT_NOTIFICATION.value,
            intervention_component_trigger=NotificationsTriggers.BEFORE_QUIT_NOTIFICATION.value),
        InterventionComponents(
            intervention_component_name=Notifications.PA_STEP_GOAL_NOTIFICATION.value,
            intervention_component_trigger=NotificationsTriggers.PA_STEP_GOAL_NOTIFICATION.value),
        InterventionComponents(
            intervention_component_name=Notifications.PA_INTENSITY_MINUTES_NOTIFICATION.value,
            intervention_component_trigger=NotificationsTriggers.PA_INTENSITY_MINUTES_NOTIFICATION.value),
        InterventionComponents(
            intervention_component_name=Notifications.QUIT_DATE_NOTIFICATION.value,
            intervention_component_trigger=NotificationsTriggers.QUIT_DATE_NOTIFICATION.value),
        InterventionComponents(intervention_component_name=Notifications.TRACK_NOTIFICATION.value,
                               intervention_component_trigger=NotificationsTriggers.TRACK_NOTIFICATION.value),
        InterventionComponents(
            intervention_component_name=Notifications.FINISH_DIALOG_NOTIFICATION.value,
            intervention_component_trigger=NotificationsTriggers.FINISH_DIALOG_NOTIFICATION.value),
        InterventionComponents(
            intervention_component_name=Notifications.INACTIVE_USER_NOTIFICATION.value,
            intervention_component_trigger=NotificationsTriggers.INACTIVE_USER_NOTIFICATION.value),
        InterventionComponents(intervention_component_name=Components.DELAYED_MSG_LAPSE.value,
                               intervention_component_trigger=ComponentsTriggers.DELAYED_MSG_LAPSE.value),
        InterventionComponents(intervention_component_name=Components.DELAYED_MSG_SMOKE.value,
                               intervention_component_trigger=ComponentsTriggers.DELAYED_MSG_SMOKE.value),
    ]

    return data


# intervention_phases table
def initialize_phases_table():
    data = [
        InterventionPhases(phase_name=Phases.PREPARATION.value),
        InterventionPhases(phase_name=Phases.EXECUTION.value),
        InterventionPhases(phase_name=Phases.LAPSE.value)
    ]

    return data


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    # docker-compose will provide the db url as environment variable. If this variable
    # cant be found, the defaults from the helper module will be used.
    session = get_db_session()

    populate_db_fixed_data(session)
    logging.info('Successfully populated database with fixed data')
