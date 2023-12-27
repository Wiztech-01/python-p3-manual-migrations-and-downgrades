"""Renaming students to scholars

Revision ID: ac8a74e1bee4
Revises: 791279dd0760
Create Date: 2023-12-12 18:31:18.295503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac8a74e1bee4'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    pass
    op.rename_table('scholars', 'students')