"""Rename column in Student model

Revision ID: 18f52d8659c9
Revises: ac8a74e1bee4
Create Date: 2023-12-12 18:47:04.090741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f52d8659c9'
down_revision = 'ac8a74e1bee4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    op.rename_column('name', 'stud_name')


def downgrade() -> None:
    pass
    op.rename_column('name', 'stud_name')