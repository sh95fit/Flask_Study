"""Added column to memo model (is_deleted)

Revision ID: 51a292caabc0
Revises: 72f8f43cd00e
Create Date: 2023-04-25 09:29:45.466793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51a292caabc0'
down_revision = '72f8f43cd00e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_deleted', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo', schema=None) as batch_op:
        batch_op.drop_column('is_deleted')

    # ### end Alembic commands ###
