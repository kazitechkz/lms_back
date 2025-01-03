"""add_feedback

Revision ID: 53cccb620123
Revises: 436b36427890
Create Date: 2025-01-03 17:28:30.820963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53cccb620123'
down_revision: Union[str, None] = '436b36427890'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'feedback',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('test_id', sa.Integer, sa.ForeignKey('tests.id'), nullable=False),
        sa.Column('question_id', sa.Integer, sa.ForeignKey('questions.id'), nullable=True),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('feedback')
