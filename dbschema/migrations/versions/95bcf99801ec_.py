"""empty message

Revision ID: 95bcf99801ec
Revises: e8be58ef0e09
Create Date: 2023-03-16 13:39:52.669057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95bcf99801ec'
down_revision = 'e8be58ef0e09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_state_machine',
    sa.Column('state_machine_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('users_nicedayuid', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('dialog_running', sa.Boolean(), nullable=True),
    sa.Column('dialog_start_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('intervention_component_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['intervention_component_id'], ['intervention_components.intervention_component_id'], ),
    sa.ForeignKeyConstraint(['users_nicedayuid'], ['users.nicedayuid'], ),
    sa.PrimaryKeyConstraint('state_machine_id')
    )
    op.add_column('users', sa.Column('start_date', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('execution_week', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'execution_week')
    op.drop_column('users', 'start_date')
    op.drop_table('user_state_machine')
    # ### end Alembic commands ###
