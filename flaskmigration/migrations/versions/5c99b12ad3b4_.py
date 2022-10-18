"""empty message

Revision ID: 5c99b12ad3b4
Revises: 85964f105ecd
Create Date: 2022-10-10 15:52:21.491211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c99b12ad3b4'
down_revision = '85964f105ecd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('topic', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'topic')
    # ### end Alembic commands ###
