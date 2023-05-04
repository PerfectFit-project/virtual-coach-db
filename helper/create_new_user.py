import logging
import os
import sys

from dbschema.models import (DialogClosedAnswers, DialogOpenAnswers, DialogQuestions, Users,
                             UserInterventionState,
                             FirstAidKit, InterventionActivity, InterventionComponents,
                             InterventionPhases,
                             ClosedAnswers, InterventionActivitiesPerformed, Testimonials,
                             StepCounts, UserStateMachine)
from helper.helper_functions import get_db_session
from datetime import datetime, date, timedelta
from dateutil import tz

tz_nl = tz.gettz("Europe/Amsterdam")


def create_user_data(user_id: int):

    db_url = os.environ['DATABASE_URL']
    session = get_db_session(db_url)
    test_data = create_test_data(user_id)

    [session.merge(obj) for obj in test_data]

    session.commit()
    logging.info("user data added to DB")


def create_test_data(user_id: int):
    data = [
        Users(dob=date(2000, 1, 2), firstname='Walter', gender='MALE', lastname='Test',
              location='Eanske', nicedayuid=user_id, testim_godin_activity_level=1,
              testim_running_walking_pref=1, testim_self_efficacy_pref=40.44,
              testim_sim_cluster_1=-2, testim_sim_cluster_3=3, week_days='1,2,3,4,5,6,7',
              preferred_time=(datetime.now().astimezone(tz_nl) + timedelta(minutes=3)),
              quit_date=date.today() + timedelta(days=11)),

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
    user_id = int(sys.argv[1])
    create_user_data(user_id)
