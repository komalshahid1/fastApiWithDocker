"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2024-04-10 15:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create user_educations table
    op.create_table(
        'user_educations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('course', sa.String(), nullable=False),
        sa.Column('class_name', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create index on user_id for better query performance
    op.create_index('ix_user_educations_user_id', 'user_educations', ['user_id'])


def downgrade() -> None:
    # Drop the table and its index
    op.drop_index('ix_user_educations_user_id', table_name='user_educations')
    op.drop_table('user_educations') 