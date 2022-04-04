import logging
import os
from datetime import datetime, date

from dbschema.models import Users, ClosedUserAnswers, UserInterventionState, DialogQuestions, DialogAnswers
from helper import get_db_session


def populate_db_with_test_data(session):
    """
    Populate the database with test data. Update data if it already exists.
    """
    # Fill question table
    objects_questions = [
        DialogQuestions(question_id=1, question_description='future self dialog - smoker words'),
        DialogQuestions(question_id=2, question_description='future self dialog - smoker why'),
        DialogQuestions(question_id=3, question_description='future self dialog - mover words'),
        DialogQuestions(question_id=4, question_description='future self dialog - mover why')
    ]
    [session.merge(obj) for obj in objects_questions]

    objects = [
        Users(dob=date(2019, 4, 13), firstname='Sven', gender='MALE', lastname='van der burg',
              location='Damsko', nicedayuid=38527),
        Users(dob=date(2018, 1, 2), firstname='Nele', gender='FEMALE', lastname='Albers',
              location='Delft', nicedayuid=40121),
        Users(dob=date(2000, 1, 2), firstname='Bouke', gender='MALE', lastname='RRD',
              location='Eanske', nicedayuid=41215),
        Users(dob=date(2000, 1, 2), firstname='User', gender='MALE', lastname='Test',
              location='Eanske', nicedayuid=41538),
        ClosedUserAnswers(users_nicedayuid=38527, value=3, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=38527, value=5, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=38527, value=4, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=40121, value=2, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=40121, value=1, question='paevaluation', datetime=datetime.now()),
        DialogAnswers(users_nicedayuid=38527, answer='lekker stoer eng', question_id=1,
                      datetime=datetime.now()),
        UserInterventionState(users_nicedayuid=40121, intervention_component="future_self_dialog", last_time=datetime.now(), last_part=1)
    ]
    [session.merge(obj) for obj in objects]

    session.commit()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    # Heroku and docker-compose will provide the db url as environment variable. If this variable
    # cant be found, the defaults from the helper module will be used.
    try:
        db_url = os.environ['SQLALCHEMY_DATABASE_URL']
        session = get_db_session(db_url)
    except KeyError:
        session = get_db_session()
    populate_db_with_test_data(session)
    logging.info('Succesfully populated database with test data')
