"""empty message

Revision ID: 110b1e4ad85f
Revises: d77ec0c12a5f
Create Date: 2021-09-09 13:21:21.417359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '110b1e4ad85f'
down_revision = 'd77ec0c12a5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('PA_evaluation', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'PA_evaluation')
    # ### end Alembic commands ###
