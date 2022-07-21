"""
Contains fixtures that are used in the unit testing framework 'pytest'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dbschema.models import Base
import pytest


@pytest.fixture(scope="session")
def engine():
    return create_engine('sqlite:///:memory:')


@pytest.fixture(scope="session")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture
def test_user_id():
    test_user_id = 41538
    return test_user_id
