from sqlalchemy.orm.clsregistry import _ModuleMarker

from dbschema.models import Base
from helper.populate_db import populate_db_fixed_data
from helper.create_new_user import create_user_data


def test_populate_db_with_test_data(db_session, test_user_id):
    """
    Test populating the database with test data.
    We enforce that for each Model some test data must be added.
    """
    populate_db_fixed_data(db_session, './utils/activities.csv',
                           './utils/testimonials_with_user_data.csv')
    create_user_data(db_session, test_user_id)
    for mapper in Base.registry.mappers:
        klass = mapper.class_
        assert db_session.query(klass).count() > 0, \
            f'Class {klass} does not have any rows populated with test data'
