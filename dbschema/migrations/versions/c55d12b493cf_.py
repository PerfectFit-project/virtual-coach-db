"""empty message

Revision ID: c55d12b493cf
Revises: aa642a5f2f2d
Create Date: 2022-03-10 07:23:31.255313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c55d12b493cf'
down_revision = 'aa642a5f2f2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_intervention_state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('users_nicedayuid', sa.Integer(), nullable=True),
    sa.Column('futureselfdialogdatetime', sa.DateTime(), nullable=True),
    sa.Column('futureselfdialogpart', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['users_nicedayuid'], ['users.nicedayuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_intervention_state')
    # ### end Alembic commands ###