from datetime import datetime, date

from dbschema.models import Users, ClosedUserAnswers
from helper import get_db_session


def populate_db_with_test_data(session):
    """
    Populate the database with test data.
    """
    session.add_all([
        Users(dob=date(2019, 4, 13), firstname='Sven', gender='MALE', lastname='van der burg',
              location='Damsko', id=38527),
        Users(dob=date(2018, 1, 2), firstname='Nele', gender='FEMALE', lastname='Albers',
              location='Delft', id=40121),
        ClosedUserAnswers(users_id=38527, value=3, question='paevaluation', datetime=datetime.now())
    ])
    session.commit()


if __name__ == '__main__':
    session = get_db_session()
    populate_db_with_test_data(session)
