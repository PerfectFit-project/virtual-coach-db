"""empty message

Revision ID: 973d60b902ed
Revises: 39447dff8c4d
Create Date: 2021-10-21 11:15:10.930107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '973d60b902ed'
down_revision = '39447dff8c4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('closed_user_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('users', 'paevaluation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('paevaluation', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_table('closed_user_answers')
    # ### end Alembic commands ###
