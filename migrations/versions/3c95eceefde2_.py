"""empty message

Revision ID: 3c95eceefde2
Revises: 4e6e9786c450
Create Date: 2021-03-08 16:34:12.728057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c95eceefde2'
down_revision = '4e6e9786c450'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('escolas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('cep', sa.String(), nullable=True),
    sa.Column('rua', sa.String(), nullable=True),
    sa.Column('complemento', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.Column('estado', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('escolas')
    # ### end Alembic commands ###
