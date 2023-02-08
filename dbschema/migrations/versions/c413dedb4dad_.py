"""empty message

Revision ID: c413dedb4dad
Revises: 28f7d1051652
Create Date: 2023-02-08 11:07:20.892696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c413dedb4dad'
down_revision = '28f7d1051652'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('quit_date', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('long_term_pa_goal', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'long_term_pa_goal')
    op.drop_column('users', 'quit_date')
    # ### end Alembic commands ###
