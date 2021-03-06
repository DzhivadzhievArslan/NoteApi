"""empty message

Revision ID: ec1b5e7f055c
Revises: 10193c6c6b08
Create Date: 2021-12-22 19:01:42.304870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec1b5e7f055c'
down_revision = '10193c6c6b08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note_model', sa.Column('archive', sa.Boolean(), server_default=sa.text('0'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note_model', 'archive')
    # ### end Alembic commands ###
