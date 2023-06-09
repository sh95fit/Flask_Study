"""Added relationship

Revision ID: 375750b966be
Revises: 493d5d6ec2a6
Create Date: 2023-04-25 16:56:43.321604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375750b966be'
down_revision = '493d5d6ec2a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memos_labels',
    sa.Column('memo_id', sa.Integer(), nullable=False),
    sa.Column('label_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.ForeignKeyConstraint(['memo_id'], ['memo.id'], ),
    sa.PrimaryKeyConstraint('memo_id', 'label_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memos_labels')
    # ### end Alembic commands ###
