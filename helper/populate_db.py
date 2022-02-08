from datetime import datetime, date

from dbschema.models import Users, ClosedUserAnswers
from helper import get_db_session


def populate_db_with_test_data(session):
    """
    Populate the database with test data.
    """
    session.add_all([
        Users(dob=date(2019, 4, 13), firstname='Sven', gender='MALE', lastname='van der burg',
              location='Damsko', nicedayuid=38527),
        Users(dob=date(2018, 1, 2), firstname='Nele', gender='FEMALE', lastname='Albers',
              location='Delft', nicedayuid=40121),
        ClosedUserAnswers(users_nicedayuid=38527, value=3, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=38527, value=5, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=38527, value=4, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=40121, value=2, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=40121, value=1, question='paevaluation', datetime=datetime.now()),
    ])
    session.commit()


if __name__ == '__main__':
    session = get_db_session()
    populate_db_with_test_data(session)