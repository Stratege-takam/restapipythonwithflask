"""Update column


Revision ID: d1c7e2101921
Revises: 90f0de122058
Create Date: 2020-07-02 09:34:20.206863

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd1c7e2101921'
down_revision = '90f0de122058'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lastconnecteAt', sa.DateTime(), nullable=True))
    op.drop_column('users', 'lastconnecteDate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lastconnecteDate', mysql.DATETIME(), nullable=True))
    op.drop_column('users', 'lastconnecteAt')
    # ### end Alembic commands ###
