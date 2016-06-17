"""empty message

Revision ID: 249cb68936ae
Revises: 5101254880c
Create Date: 2016-06-17 22:02:04.578000

"""

# revision identifiers, used by Alembic.
revision = '249cb68936ae'
down_revision = '5101254880c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sharepoint_server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_sharepoint_server_name', 'sharepoint_server', ['name'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_sharepoint_server_name', 'sharepoint_server')
    op.drop_table('sharepoint_server')
    ### end Alembic commands ###
