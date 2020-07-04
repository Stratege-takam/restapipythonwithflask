"""Suppression du hiredate

Revision ID: feb9fb336cc8
Revises: 6de43b978e9c
Create Date: 2020-07-02 20:47:44.761232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'feb9fb336cc8'
down_revision = '6de43b978e9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('professors', 'hiredate')
    op.drop_column('professors', 'testadd')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professors', sa.Column('testadd', mysql.FLOAT(), nullable=True))
    op.add_column('professors', sa.Column('hiredate', sa.DATE(), nullable=True))
    # ### end Alembic commands ###