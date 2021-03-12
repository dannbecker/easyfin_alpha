"""empty message

Revision ID: e1b68653ce8c
Revises: 3c95eceefde2
Create Date: 2021-03-08 18:09:34.918063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1b68653ce8c'
down_revision = '3c95eceefde2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('escolas', sa.Column('bairro', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('escolas', 'bairro')
    # ### end Alembic commands ###