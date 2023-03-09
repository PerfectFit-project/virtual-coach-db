from enum import Enum


class Phases(str, Enum):
    PREPARATION = 'preparation'
    EXECUTION = 'execution'
    LAPSE = 'lapse'


class Components(str, Enum):
    PREPARATION_INTRODUCTION = 'preparation_introduction'
    PROFILE_CREATION = 'profile_creation'
    MEDICATION_TALK = 'medication_talk'
    TRACK_BEHAVIOR = 'track_behavior'
    COLD_TURKEY = 'cold_turkey'
    PLAN_QUIT_START_DATE = 'plan_quit_start_date'
    FUTURE_SELF_LONG = 'future_self_long'
    FUTURE_SELF_SHORT = 'future_self_short'
    GOAL_SETTING = 'goal_setting'
    FIRST_AID_KIT_VIDEO = 'first_aid_kit_video'
    EXECUTION_INTRODUCTION = 'execution_introduction'
    GENERAL_ACTIVITY = 'general_activity'
    WEEKLY_REFLECTION = 'weekly_reflection'
    DAILY_REFLECTION = 'daily_reflection'
    RELAPSE_DIALOG = 'relapse_dialog'
    RELAPSE_DIALOG_HRS = 'relapse_dialog_hrs'
    RELAPSE_DIALOG_LAPSE = 'relapse_dialog_lapse'
    RELAPSE_DIALOG_RELAPSE = 'relapse_dialog_relapse'
    RELAPSE_DIALOG_PA = 'relapse_dialog_pa'
    FIRST_AID_KIT = 'get_first_aid_kit'
    CLOSING_DIALOG = 'closing_dialog'
    RESCHEDULING_PREPARATION = 'rescheduling_preparation_phase'
    WATCH_VIDEO = 'watch_video_dialog'


class ComponentsTriggers(str, Enum):
    PREPARATION_INTRODUCTION = 'EXTERNAL_trigger_preparation_introduction'
    PROFILE_CREATION = 'EXTERNAL_trigger_profile_creation'
    MEDICATION_TALK = 'EXTERNAL_trigger_medication_talk'
    TRACK_BEHAVIOR = 'EXTERNAL_trigger_track_behavior'
    COLD_TURKEY = 'EXTERNAL_trigger_cold_turkey'
    PLAN_QUIT_START_DATE = 'EXTERNAL_trigger_plan_quit_start'
    FUTURE_SELF_LONG = 'EXTERNAL_trigger_future_self_long'
    FUTURE_SELF_SHORT = 'EXTERNAL_trigger_future_self_short'
    GOAL_SETTING = 'EXTERNAL_trigger_goal_setting'
    FIRST_AID_KIT_VIDEO = 'EXTERNAL_first_aid_kit_video'
    EXECUTION_INTRODUCTION = 'EXTERNAL_trigger_execution_introduction'
    GENERAL_ACTIVITY = 'EXTERNAL_trigger_general_activity'
    WEEKLY_REFLECTION = 'EXTERNAL_weekly_reflection'
    DAILY_REFLECTION = 'EXTERNAL_daily_reflection'
    RELAPSE_DIALOG = 'EXTERNAL_relapse_dialog'
    RELAPSE_DIALOG_HRS = 'EXTERNAL_relapse_dialog_hrs'
    RELAPSE_DIALOG_LAPSE = 'EXTERNAL_relapse_dialog_lapse'
    RELAPSE_DIALOG_RELAPSE = 'EXTERNAL_relapse_dialog_relapse'
    RELAPSE_DIALOG_PA = 'EXTERNAL_relapse_dialog_pa'
    FIRST_AID_KIT = 'CENTRAL_get_first_aid_kit'
    CLOSING_DIALOG = 'EXTERNAL_closing_dialog'
    RESCHEDULING_PREPARATION = 'EXTERNAL_rescheduling_preparation_phase'
    WATCH_VIDEO = 'EXTERNAL_watch_video_dialog'


class Notifications(str, Enum):
    BEFORE_QUIT_NOTIFICATION = 'before_quit_notification'
    PA_NOTIFICATION = 'pa_notification'
    QUIT_DATE_NOTIFICATION = 'quit_date_notification'
    TRACK_NOTIFICATION = 'track_notification'


class NotificationsTriggers(str, Enum):
    BEFORE_QUIT_NOTIFICATION = 'EXTERNAL_before_quit_notification'
    PA_NOTIFICATION = 'EXTERNAL_pa_notification'
    QUIT_DATE_NOTIFICATION = 'EXTERNAL_quit_date_notification'
    TRACK_NOTIFICATION = 'EXTERNAL_trigger_track_notification'


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
    RELAPSE_CRAVING_REFLECT_BARCHART = 11
    RELAPSE_LAPSE_TYPE_SMOKE = 12
    RELAPSE_LAPSE_NUMBER_CIGARETTES = 13
    RELAPSE_LAPSE_WHAT_DOING = 14
    RELAPSE_LAPSE_HOW_FEEL = 15
    RELAPSE_LAPSE_WITH_WHOM = 16
    RELAPSE_LAPSE_HAPPENED_SPECIAL = 17
    RELAPSE_LAPSE_REFLECT_BARCHART = 18
    RELAPSE_RELAPSE_TYPE_SMOKE = 19
    RELAPSE_RELAPSE_NUMBER_CIGARETTES = 20
    RELAPSE_RELAPSE_WHAT_DOING = 21
    RELAPSE_RELAPSE_HOW_FEEL = 22
    RELAPSE_RELAPSE_WITH_WHOM = 23
    RELAPSE_RELAPSE_HAPPENED_SPECIAL = 24
    RELAPSE_RELAPSE_REFLECT_BARCHART = 25
    RELAPSE_PA_SPECIFY_PA = 26  # Kun je mij vertellen wat er aan de hand is?
    RELAPSE_PA_TYPE = 27  # Kun je mij vertellen wat voor lichamelijke activiteit je had gepland om te doen?
    RELAPSE_PA_TOGETHER = 28  # Zou je dit met iemand samen doen?
    RELAPSE_PA_WHY_FAIL = 29  # Kun je aangeven wat de reden is dat dat je nu niet lukt?
    RELAPSE_PA_DOING_TODAY = 30  # Wat heb je vandaag verder gedaan?
    RELAPSE_PA_HAPPENED_SPECIAL = 31  # Gebeurde er vandaag iets bijzonders?
    RELAPSE_PA_REFLECT_BARCHART = 32  # Hoe vind je het om dit zo te zien?
    PERSUASION_PROMPTS = 33  # Whether people have prompts/triggers to remind them to do an activity
    PERSUASION_WANT = 34  # Whether people feel like they want to to do the activity
    PERSUASION_NEED = 35  # Whether people feel like they need to do the activity
    PERSUASION_EFFORT = 36  # How much effort people spent on an activity
    PERSUASION_TYPE = 37  # The persuasion type chosen based on the persuasion algorithm
    PERSUASION_MESSAGE_INDEX = 38  # The index of the persuasive message for the given persuasion type. -1 if "No persuasion."


class VideoLinks(str, Enum):
    # TODO: substitute the links with the actual one
    BACK_TO_NICEDAY = "back to niceday"
    FIRST_AID_KIT = "first aid kit"
    FUTURE_SELF_LONG = 'future self long'
    FUTURE_SELF_SHORT = 'future self short'
    INTRO_EXECUTION_VIDEO = "Intro execution video"
    INTRO_PREPARATION_VIDEO = "preparation link"
    MEDICATION_VIDEO = "https://www.youtube.com/watch?v=59JaTljpjCk"
    TRACKING_BEHAVIORS = "tracking behaviors"
    TESTVIDEOLINK = "testLink"


"""Dictionary for the expected time interval of the dialog"""
DialogExpectedDuration = {Components.PREPARATION_INTRODUCTION: (1, 6),
                          Components.PROFILE_CREATION: (2, 3),
                          Components.MEDICATION_TALK: (4, 9),
                          Components.TRACK_BEHAVIOR: (5, 7),
                          Components.FUTURE_SELF_LONG: (5, 10)}
