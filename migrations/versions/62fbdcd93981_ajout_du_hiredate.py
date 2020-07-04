"""ajout du hiredate

Revision ID: 62fbdcd93981
Revises: ac7563cde074
Create Date: 2020-07-02 20:56:14.301184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62fbdcd93981'
down_revision = 'ac7563cde074'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professors', sa.Column('hiredate', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('professors', 'hiredate')
    # ### end Alembic commands ###
