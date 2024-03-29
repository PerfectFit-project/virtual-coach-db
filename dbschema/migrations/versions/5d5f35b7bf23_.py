"""empty message

Revision ID: 5d5f35b7bf23
Revises: 95bcf99801ec
Create Date: 2023-05-02 09:15:20.105571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5f35b7bf23'
down_revision = '95bcf99801ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('goal_setting_chosen_sport', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'goal_setting_chosen_sport')
    # ### end Alembic commands ###
