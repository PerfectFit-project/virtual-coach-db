from sqlalchemy.orm.clsregistry import _ModuleMarker

from dbschema.models import Base
from helper.populate_db import populate_db_with_test_data


def test_populate_db_with_test_data(db_session):
    """
    Test populating the database with test data.
    We enforce that for each Model some test data must be added.
    """
    populate_db_with_test_data(db_session)
    # Go through all SQLAlchemy models
    for name, klass in Base._decl_class_registry.items():
        if isinstance(klass, _ModuleMarker):
            # Not a model
            continue
        assert db_session.query(klass).count() > 0, \
            f'Class {klass} does not have any rows populated with test data'
