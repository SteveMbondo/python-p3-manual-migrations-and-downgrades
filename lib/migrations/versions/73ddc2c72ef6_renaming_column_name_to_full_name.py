"""Renaming column name to full_name

Revision ID: 73ddc2c72ef6
Revises: b9c29eb574e3
Create Date: 2024-01-09 17:33:12.663641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ddc2c72ef6'
down_revision = 'b9c29eb574e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('scholars', 'full_name', new_column_name='name')
