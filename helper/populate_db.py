from datetime import datetime, date

from dbschema.models import Users, ClosedUserAnswers, DialogAnswers, DialogQuestions
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
        Users(dob=date(2000, 1, 2), firstname='Bouke', gender='MALE', lastname='RRD',
              location='Eanske', nicedayuid=41215),
        ClosedUserAnswers(users_nicedayuid=38527, value=3, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=38527, value=5, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=38527, value=4, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=40121, value=2, question='paevaluation', datetime=datetime.now()),
        ClosedUserAnswers(users_nicedayuid=40121, value=1, question='paevaluation', datetime=datetime.now()),
        DialogAnswers(users_nicedayuid=38527, answer='lekker stoer eng', question_id=1, datetime=datetime.now())
    ])

    # Fill question table
    session.add_all([
        DialogQuestions(question_id=1, question_description='future self dialog - smoker words'),
        DialogQuestions(question_id=2, question_description='future self dialog - smoker why'),
        DialogQuestions(question_id=3, question_description='future self dialog - mover words'),
        DialogQuestions(question_id=4, question_description='future self dialog - mover why')
    ])

    session.commit()

if __name__ == '__main__':
    session = get_db_session(db_host='localhost:5432')
    populate_db_with_test_data(session)
    # New function with fill up DialogQuestions table?
