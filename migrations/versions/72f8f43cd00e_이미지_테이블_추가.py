"""이미지 테이블 추가

Revision ID: 72f8f43cd00e
Revises: 20239bfa99b0
Create Date: 2023-04-21 14:35:04.093893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72f8f43cd00e'
down_revision = '20239bfa99b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linked_image', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('memo', schema=None) as batch_op:
        batch_op.drop_column('linked_image')

    # ### end Alembic commands ###
