"""empty message

Revision ID: c7af1944414c
Revises: dcd3663ba17d
Create Date: 2022-12-09 11:45:28.936949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7af1944414c'
down_revision = 'dcd3663ba17d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('intervention_activity', sa.Column('intervention_activity_benefit', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('intervention_activity', 'intervention_activity_benefit')
    # ### end Alembic commands ###
