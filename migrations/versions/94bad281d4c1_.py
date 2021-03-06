"""empty message

Revision ID: 94bad281d4c1
Revises: 2e47e1d1258e
Create Date: 2021-03-01 19:33:09.535897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94bad281d4c1'
down_revision = '2e47e1d1258e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
