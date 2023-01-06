"""empty message

Revision ID: 829c70a6dadd
Revises: 
Create Date: 2023-01-05 13:53:40.286574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '829c70a6dadd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('board_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'board', ['board_id'], ['board_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'board_id')
    # ### end Alembic commands ###
