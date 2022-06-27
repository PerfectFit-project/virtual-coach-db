import sys

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from dbschema.models import InterventionComponents

DB_URL_DEFAULT = 'postgresql://root:root@db:5432/perfectfit'

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

def get_db_session(db_url=DB_URL_DEFAULT):

    sanitized_db_url = santize_db_url(db_url)
    engine = create_engine(sanitized_db_url)
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

def get_intervention_component_id(intervention_component_name: str, db_url=DB_URL_DEFAULT) -> int:
    """
       Get the id of an intervention component as stored in the DB
        from the intervention's name.

    """
    session = get_db_session(db_url)

    selected = (
        session.query(
            InterventionComponents
        )
        .filter(
            InterventionComponents.intervention_component_name == intervention_component_name
        )
        .all()
    )

    intervention_component_id = selected[0].intervention_component_id
    return intervention_component_id
