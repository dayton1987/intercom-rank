"""empty message

Revision ID: ef6edca55d1d
Revises: 73bc969a393a
Create Date: 2016-01-25 16:29:29.840699

"""

# revision identifiers, used by Alembic.
revision = 'ef6edca55d1d'
down_revision = '73bc969a393a'

from alembic import op
import sqlalchemy as sa
from funcy import chunks

from app import FREE_EMAILS_SET


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    table = op.create_table('free_email_providers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain', sa.Unicode(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_free_email_providers_domain'), 'free_email_providers', ['domain'], unique=False)
    ### end Alembic commands ###

    # Fill the data
    for domains in chunks(1000, FREE_EMAILS_SET):
        op.bulk_insert(table, [{'domain': d} for d in domains])


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_free_email_providers_domain'), table_name='free_email_providers')
    op.drop_table('free_email_providers')
    ### end Alembic commands ###
