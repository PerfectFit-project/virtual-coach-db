import json
import logging

import importlib_resources
import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    DATABASE_URL = 'postgresql://root:root@db:5432/perfectfit'


def santize_db_url(db_url):
    """
    SQLAlchemy cannot handle the "postgres" prefix
    (see https://github.com/sqlalchemy/sqlalchemy/issues/6083), but Heroku still populates
    DATABASE_URL with that protocol designator. For such URLs we need to modify the string
    from "postgres" -> "postgresql".

    We are doing this string replacement because the config var DATABASE_URL provided by
    Heroku may change.
    """
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    return db_url


def init_engine():
    try:
        # initialize engine and session maker
        engine = create_engine(santize_db_url(DATABASE_URL), poolclass=NullPool)
        meta = MetaData()
        meta.reflect(bind=engine)

        return sessionmaker(bind=engine)
    except:
        logging.error('Connection to DB failed. Empty session maker')
        return None


session_maker = init_engine()


def get_db_session():
    global session_maker

    if not session_maker:
        session_maker = init_engine()

    session = session_maker()

    return session


def get_timing():
    string_json = importlib_resources.files('virtual_coach_db').joinpath(
        'resources/resources_timing.json').read_text()

    timing = json.loads(string_json)

    return timing
