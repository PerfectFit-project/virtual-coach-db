import logging
from datetime import datetime, date

from dbschema.models import Users, ClosedUserAnswers, UserInterventionState
from helper import get_db_session


def populate_db_with_test_data(session):
    """
    Populate the database with test data. Update data if it already exists.
    """
    objects = [
        Users(dob=date(2019, 4, 13), firstname='Sven', gender='MALE', lastname='van der burg',
              location='Damsko', nicedayuid=38527),
        Users(dob=date(2018, 1, 2), firstname='Nele', gender='FEMALE', lastname='Albers',
              location='Delft', nicedayuid=40121),
        ClosedUserAnswers(id=1, users_nicedayuid=38527, value=3, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(id=2, users_nicedayuid=38527, value=5, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(id=3, users_nicedayuid=38527, value=4, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(id=4, users_nicedayuid=40121, value=2, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(id=5, users_nicedayuid=40121, value=1, question='paevaluation', datetime=datetime.now()),
        UserInterventionState(id=1, users_nicedayuid=40121, intervention_component="future_self_dialog", last_time=datetime.now(), last_part="step_1"),
    ]
    [session.merge(obj) for obj in objects]
    session.commit()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    #session = get_db_session()
    session = get_db_session(db_host='localhost:5432')
    populate_db_with_test_data(session)
    logging.info('Succesfully populated database with test data')
