"""ajout du hiredate

Revision ID: ae9540b2005d
Revises: 266afbf55b0c
Create Date: 2020-07-02 23:20:39.313849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae9540b2005d'
down_revision = '266afbf55b0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authjwts', sa.Column('token', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authjwts', 'token')
    # ### end Alembic commands ###