"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2025-04-09 12:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
   if not op.get_bind().dialect.has_table(op.get_bind(), 'users'):
        op.create_table(
            'users',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(255), nullable=False),
            sa.Column('email', sa.String(255), nullable=False, unique=True),
        )

def downgrade():
    op.drop_table('users')
