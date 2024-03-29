"""empty message

Revision ID: 7a9917098603
Revises: 2cf4a55505b7
Create Date: 2023-02-22 10:06:34.290905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a9917098603'
down_revision = '2cf4a55505b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('step_counts',
    sa.Column('step_count_id', sa.Integer(), nullable=False),
    sa.Column('users_nicedayuid', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['users_nicedayuid'], ['users.nicedayuid'], ),
    sa.PrimaryKeyConstraint('step_count_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('step_counts')
    # ### end Alembic commands ###
