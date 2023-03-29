"""Added datatime column to user model

Revision ID: 939aee29af94
Revises: 7f1ed7eacb7c
Create Date: 2023-03-29 14:51:50.653269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '939aee29af94'
down_revision = '7f1ed7eacb7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True, server_defalut=sa.text('now()')))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
