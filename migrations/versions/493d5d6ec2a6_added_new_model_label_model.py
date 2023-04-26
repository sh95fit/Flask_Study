"""Added new model (label model)

Revision ID: 493d5d6ec2a6
Revises: 51a292caabc0
Create Date: 2023-04-25 11:12:59.676526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493d5d6ec2a6'
down_revision = '51a292caabc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content', 'user_id', name='uk_content_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('label')
    # ### end Alembic commands ###