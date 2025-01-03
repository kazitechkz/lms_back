"""add_questions

Revision ID: 13d4ce32ba0a
Revises: c2a5070fddd9
Create Date: 2025-01-03 16:19:46.512545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13d4ce32ba0a'
down_revision: Union[str, None] = 'c2a5070fddd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('test_id', sa.Integer, sa.ForeignKey('tests.id'), nullable=False),
        sa.Column('text', sa.Text, nullable=False),
        sa.Column('hint', sa.Text, nullable=True),
        sa.Column('explanation', sa.Text, nullable=True),
        sa.Column('type', sa.String(length=256), nullable=False),
        sa.Column('points', sa.Float, default=1.0)
    )


def downgrade() -> None:
    op.drop_table('questions')
