"""empty message

Revision ID: 28f7d1051652
Revises: be53ab5e40fa
Create Date: 2023-01-23 14:37:42.428261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f7d1051652'
down_revision = 'be53ab5e40fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testimonials', sa.Column('part_of_cluster1', sa.Boolean(), nullable=True))
    op.add_column('testimonials', sa.Column('part_of_cluster3', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testimonials', 'part_of_cluster3')
    op.drop_column('testimonials', 'part_of_cluster1')
    # ### end Alembic commands ###
