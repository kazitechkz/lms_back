"""add_tests

Revision ID: c2a5070fddd9
Revises: e43b193eb74d
Create Date: 2025-01-03 16:18:27.588599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2a5070fddd9'
down_revision: Union[str, None] = 'e43b193eb74d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tests',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=256), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('type', sa.Enum('TEST', 'EXAM', name='testtype'), nullable=False),
        sa.Column('is_demo', sa.Boolean, default=False),
        sa.Column('organization_id', sa.Integer, sa.ForeignKey('organizations.id'), nullable=True),
        sa.Column('course_id', sa.Integer, nullable=True),  # Связь с курсами (если потребуется)
        sa.Column('time_limit', sa.Integer, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('tests')

    # Drop ENUM type
    sa.Enum(name='testtype').drop(op.get_bind())
