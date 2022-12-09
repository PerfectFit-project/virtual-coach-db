from enum import Enum


class Phases(str, Enum):
    PREPARATION = 'preparation'
    EXECUTION = 'execution'
    LAPSE = 'lapse'


class PreparationInterventionComponents(str, Enum):
    PROFILE_CREATION = 'profile_creation'
    MEDICATION_TALK = 'medication_talk'
    COLD_TURKEY = 'cold_turkey'
    PLAN_QUIT_START_DATE = 'plan_quit_start_date'
    FUTURE_SELF = 'future_self_preparation'
    GOAL_SETTING = 'goal_setting'


class PreparationInterventionComponentsTriggers(str, Enum):
    PROFILE_CREATION = 'EXTERNAL_trigger_profile_creation'
    MEDICATION_TALK = 'EXTERNAL_trigger_medication_talk'
    COLD_TURKEY = 'EXTERNAL_trigger_cold_turkey'
    PLAN_QUIT_START_DATE = 'EXTERNAL_trigger_plan_quit_start'
    FUTURE_SELF = 'EXTERNAL_trigger_mental_contrasting'
    GOAL_SETTING = 'EXTERNAL_trigger_goal_setting'


class ExecutionInterventionComponents(str, Enum):
    EXECUTION_INTRODUCTION = 'execution_introduction'
    GENERAL_ACTIVITY = 'general_activity'
    WEEKLY_REFLECTION = 'weekly_reflection'
    DAILY_REFLECTION = 'daily_reflection'
    RELAPSE_DIALOG = 'relapse_dialog'
    RELAPSE_DIALOG_HRS = 'relapse_dialog_hrs'
    RELAPSE_DIALOG_LAPSE = 'relapse_dialog_lapse'
    RELAPSE_DIALOG_RELAPSE = 'relapse_dialog_relapse'
    RELAPSE_DIALOG_PA = 'relapse_dialog_pa'


class ExecutionInterventionComponentsTriggers(str, Enum):
    EXECUTION_INTRODUCTION = 'EXTERNAL_trigger_execution_introduction'
    GENERAL_ACTIVITY = 'EXTERNAL_trigger_general_activity'
    WEEKLY_REFLECTION = 'EXTERNAL_weekly_reflection'
    DAILY_REFLECTION = 'EXTERNAL_daily_reflection'
    RELAPSE_DIALOG = 'EXTERNAL_relapse_dialog'
    RELAPSE_DIALOG_HRS = 'EXTERNAL_relapse_dialog_hrs'
    RELAPSE_DIALOG_LAPSE = 'EXTERNAL_relapse_dialog_lapse'
    RELAPSE_DIALOG_RELAPSE = 'EXTERNAL_relapse_dialog_relapse'
    RELAPSE_DIALOG_PA = 'EXTERNAL_relapse_dialog_pa'


class DialogQuestionsEnum(Enum):
    FUTURE_SELF_SMOKER_WORDS = 1  # Which three words suits you as smoker?
    FUTURE_SELF_SMOKER_WHY = 2  # Why did you pick these words for smoking?
    FUTURE_SELF_MOVER_WORDS = 3  # Which three words suits you as exerciser?
    FUTURE_SELF_MOVER_WHY = 4  # Why did you pick these words for exercising?
    FUTURE_SELF_I_SEE_MYSELF_AS_SMOKER = 5  # I see myself as smoker, non-smoker or quitter
    FUTURE_SELF_I_SEE_MYSELF_AS_MOVER = 6  # I see myself as active, bit active or not active
    RELAPSE_CRAVING_WHAT_DOING = 7
    RELAPSE_CRAVING_HOW_FEEL = 8
    RELAPSE_CRAVING_WITH_WHOM = 9
    RELAPSE_CRAVING_HAPPENED_SPECIAL = 10
    RELAPSE_LAPSE_TYPE_SMOKE = 11
    RELAPSE_LAPSE_NUMBER_CIGARETTES = 12
    RELAPSE_LAPSE_WHAT_DOING = 13
    RELAPSE_LAPSE_HOW_FEEL = 14
    RELAPSE_LAPSE_WITH_WHOM = 15
    RELAPSE_LAPSE_HAPPENED_SPECIAL = 16
    RELAPSE_RELAPSE_TYPE_SMOKE = 17
    RELAPSE_RELAPSE_NUMBER_CIGARETTES = 18
    RELAPSE_RELAPSE_WHAT_DOING = 19
    RELAPSE_RELAPSE_HOW_FEEL = 20
    RELAPSE_RELAPSE_WITH_WHOM = 21
    RELAPSE_RELAPSE_HAPPENED_SPECIAL = 22
    RELAPSE_PA_SPECIFY_PA = 23  # Kun je mij vertellen wat er aan de hand is?
    RELAPSE_PA_TYPE = 24  # Kun je mij vertellen wat voor lichamelijke activiteit je had gepland om te doen?
    RELAPSE_PA_TOGETHER = 25  # Zou je dit met iemand samen doen?
    RELAPSE_PA_WHY_FAIL = 26  # Kun je aangeven wat de reden is dat dat je nu niet lukt?
    RELAPSE_PA_DOING_TODAY = 27  # Wat heb je vandaag verder gedaan?
    RELAPSE_PA_HAPPENED_SPECIAL = 28  # Gebeurde er vandaag iets bijzonders?
    RELAPSE_PA_REFLECT_BARCHART = 29  # Hoe vind je het om dit zo te zien?
