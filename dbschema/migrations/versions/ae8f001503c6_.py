"""empty message

Revision ID: ae8f001503c6
Revises: 28f7d1051652
Create Date: 2023-02-08 15:32:09.439541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae8f001503c6'
down_revision = '28f7d1051652'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('first_aid_kit', 'user_activity_title')
    op.drop_column('first_aid_kit', 'user_activity_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('first_aid_kit', sa.Column('user_activity_description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('first_aid_kit', sa.Column('user_activity_title', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###