"""add_answers

Revision ID: 436b36427890
Revises: 37e227e9d6fa
Create Date: 2025-01-03 16:23:00.910434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '436b36427890'
down_revision: Union[str, None] = '37e227e9d6fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'answers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('question_id', sa.Integer, sa.ForeignKey('questions.id'), nullable=False),
        sa.Column('text', sa.String(length=256), nullable=False),
        sa.Column('is_correct', sa.Boolean, default=False),
        sa.Column('characteristic_id', sa.Integer, sa.ForeignKey('characteristics.id'), nullable=True),
        sa.Column('points', sa.Float, default=0.0)
    )


def downgrade() -> None:
    op.drop_table('answers')
