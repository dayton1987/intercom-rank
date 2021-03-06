"""empty message

Revision ID: 080002be4a97
Revises: 50b85c2a8f04
Create Date: 2016-01-07 14:35:20.478665

"""

# revision identifiers, used by Alembic.
revision = '080002be4a97'
down_revision = '50b85c2a8f04'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Unicode(length=255), nullable=False),
    sa.Column('intercom_app_id', sa.Unicode(length=255), nullable=False),
    sa.Column('intercom_api_key', sa.Unicode(length=255), nullable=False),
    sa.Column('aws_access_id', sa.Unicode(length=255), nullable=False),
    sa.Column('aws_secret_access_key', sa.Unicode(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('aws_access_id'),
    sa.UniqueConstraint('intercom_app_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    ### end Alembic commands ###
