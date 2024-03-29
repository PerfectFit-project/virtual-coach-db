import logging
import os
import sys

from dbschema.models import (DialogClosedAnswers, DialogOpenAnswers, Users,
                                              UserInterventionState, FirstAidKit,
                                              InterventionActivitiesPerformed,
                                              StepCounts, UserStateMachine)
from helper.helper_functions import get_db_session
from datetime import datetime, date, timedelta
from dateutil import tz

tz_nl = tz.gettz("Europe/Amsterdam")


def create_user_data(db_session, user_id: int):
    test_data = create_test_data(user_id)

    [db_session.merge(obj) for obj in test_data]

    db_session.commit()
    logging.info("user data added to DB")


def create_test_data(user_id: int):
    data = [
        Users(nicedayuid=user_id, testim_godin_activity_level=1,
              testim_running_walking_pref=1, testim_self_efficacy_pref=40.44,
              testim_sim_cluster_1=-2, testim_sim_cluster_3=3, week_days='1,2,3,4,5,6,7',
              preferred_time=(datetime.now().astimezone(tz_nl) + timedelta(minutes=3)),
              quit_date=date.today() + timedelta(days=11), pa_steps_daily_goal=8200,
              pa_intensity_minutes_weekly_goal=70, pa_intervention_group=1),

        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=28,
                    datetime=datetime.now().astimezone(tz_nl),
                    activity_rating=1),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=32,
                    datetime=datetime.now().astimezone(tz_nl),
                    activity_rating=2),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=34,
                    datetime=datetime.now().astimezone(tz_nl),
                    activity_rating=3),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=210,
                    datetime=datetime.now().astimezone(tz_nl),
                    activity_rating=4),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=22,
                    datetime=datetime.now().astimezone(tz_nl),
                    activity_rating=5),
        FirstAidKit(users_nicedayuid=user_id, intervention_activity_id=23,
                    datetime=datetime.now().astimezone(tz_nl),
                    activity_rating=6),

        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='Fijn plezierig helpt mij ',
                          question_id=1,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id,
                          answer_value='onderdeel van mijn leven verslavend niet zo heel erg',
                          question_id=1, datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='stressvol straf lastig ',
                          question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='lastig', question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id,
                          answer_value='moet voor mijn gezondheid prettig', question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogOpenAnswers(users_nicedayuid=user_id, answer_value='moet voor mijn gezondheid goed',
                          question_id=3,
                          datetime=datetime.now().astimezone(tz_nl)),
        DialogClosedAnswers(users_nicedayuid=user_id, closed_answers_id=803,
                            datetime=datetime.now().astimezone(tz_nl)),
        DialogClosedAnswers(users_nicedayuid=user_id, closed_answers_id=1401,
                            datetime=datetime.now().astimezone(tz_nl)),
        UserInterventionState(users_nicedayuid=user_id, intervention_phase_id=1,
                              intervention_component_id=5,
                              completed=False, last_time=datetime.now().astimezone(tz_nl),
                              last_part=1),

        InterventionActivitiesPerformed(users_nicedayuid=user_id, intervention_activity_id=28,
                                        user_input='test input'),

        StepCounts(users_nicedayuid=user_id, value=5),

        UserStateMachine(users_nicedayuid=user_id,
                         state='Onboarding',
                         dialog_running=False,
                         intervention_component_id=1)
    ]

    return data


if __name__ == "__main__":
    try:
        test_user_id = int(sys.argv[1])
    except IndexError:
        test_user_id = os.environ['TEST_USER_ID']
    session = get_db_session()

    create_user_data(session, test_user_id)
    logging.info('Successfully populated database with fixed data')