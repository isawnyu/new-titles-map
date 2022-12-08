"""empty message

Revision ID: 983bb8c78a9d
Revises: 
Create Date: 2019-05-23 10:31:59.106646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '983bb8c78a9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newtitles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('precision_code', sa.Integer(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('pleiades_id', sa.String(), nullable=True),
    sa.Column('latitude', sa.Numeric(), nullable=True),
    sa.Column('longitude', sa.Numeric(), nullable=True),
    sa.Column('bsn', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('newtitles')
    # ### end Alembic commands ###