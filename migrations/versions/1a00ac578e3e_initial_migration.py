"""initial migration

Revision ID: 1a00ac578e3e
Revises: None
Create Date: 2016-06-19 21:14:35.258000

"""

# revision identifiers, used by Alembic.
revision = '1a00ac578e3e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('onboard_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('software_product', sa.String(length=64), nullable=True),
    sa.Column('sharepoint_path', sa.Text(), nullable=True),
    sa.Column('milestone_name', sa.String(length=64), nullable=True),
    sa.Column('test_cycle', sa.String(length=24), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('requester', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sharepoint_server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_sharepoint_server_name', 'sharepoint_server', ['name'], unique=True)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_username', 'users')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_index('ix_sharepoint_server_name', 'sharepoint_server')
    op.drop_table('sharepoint_server')
    op.drop_table('onboard_request')
    ### end Alembic commands ###