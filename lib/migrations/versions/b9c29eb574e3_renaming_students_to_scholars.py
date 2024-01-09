"""Renaming students to scholars

Revision ID: b9c29eb574e3
Revises: 791279dd0760
Create Date: 2024-01-09 16:38:35.778414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9c29eb574e3'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
