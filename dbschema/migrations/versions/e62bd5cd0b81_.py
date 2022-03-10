"""empty message

Revision ID: e62bd5cd0b81
Revises: a72e609148ed
Create Date: 2022-03-10 16:23:40.270201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e62bd5cd0b81'
down_revision = 'a72e609148ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_intervention_state', 'users_nicedayuid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_intervention_state', 'intervention_component',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('user_intervention_state', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_intervention_state', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.alter_column('user_intervention_state', 'intervention_component',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user_intervention_state', 'users_nicedayuid',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
