import sys

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'postgresql://root:root@db:5432/perfectfit'


def get_db_session(db_url=DB_URL):
    engine = create_engine(db_url)
    meta = MetaData()
    meta.reflect(bind=engine)

    # Check that db actually has a Users table
    # (have the alembic migrations been run to set it up appropriately?)
    if 'users' not in meta.tables:
        sys.exit('"users" table not found in db. Has the schema been '
                 'set up correctly with the alembic migrations? See '
                 'instructions in README in db/ directory.')

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    return session
