"""empty message

Revision ID: 7e27f532b452
Revises: b680a79956d3
Create Date: 2016-01-10 09:58:27.556947

"""

# revision identifiers, used by Alembic.
revision = '7e27f532b452'
down_revision = 'b680a79956d3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('intercom_subscription_id', sa.Unicode(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'intercom_subscription_id')
    ### end Alembic commands ###