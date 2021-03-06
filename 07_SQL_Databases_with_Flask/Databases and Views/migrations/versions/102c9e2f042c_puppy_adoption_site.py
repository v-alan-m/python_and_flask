"""puppy adoption site

Revision ID: 102c9e2f042c
Revises: 
Create Date: 2020-02-17 12:22:16.026109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102c9e2f042c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
