import logging
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from dbschema.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

logger = logging.getLogger(__name__)
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    logging.info('Running migrations in offline mode')
    url = get_db_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def get_db_url():
    """
    Retrieves db url from environment variable `DATABASE_URL`
    The environment variable DATABASE_URL is automatically filled in by Heroku. Unfortunately it
    has the prefix "postgres" instead of "postgresql". SQLAlchemy cannot handle the "postgres"
    prefix (deprecated: see https://github.com/sqlalchemy/sqlalchemy/issues/6083) so we need to
    modify the string from postgres -> postgresql.

    We are doing this string replacement because the config var DATABASE_URL provided by
    heroku may change.
    """
    db_url = os.environ['DATABASE_URL']
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    return db_url


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    logging.info('Running migrations in online mode')
    connectable = context.config.attributes.get("connection", None)

    if connectable is None:
        engine_config = {'sqlalchemy.url': get_db_url()}
        connectable = engine_from_config(engine_config,
                                         prefix="sqlalchemy.",
                                         poolclass=pool.NullPool,
                                         )


    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
