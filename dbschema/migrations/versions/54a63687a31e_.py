"""empty message

Revision ID: 54a63687a31e
Revises: 371db19fa5b8
Create Date: 2023-01-18 10:22:44.783578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54a63687a31e'
down_revision = '371db19fa5b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testimonials',
    sa.Column('testimonial_id', sa.Integer(), nullable=False),
    sa.Column('godin_activity_level', sa.Integer(), nullable=True),
    sa.Column('running_walking_pref', sa.Integer(), nullable=True),
    sa.Column('self_efficacy_pref', sa.Float(), nullable=True),
    sa.Column('testimonial_text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('testimonial_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testimonials')
    # ### end Alembic commands ###
