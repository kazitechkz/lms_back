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
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('is_correct', sa.Boolean, default=False),
        sa.Column('characteristic_id', sa.Integer, nullable=True),
        sa.Column('points', sa.Float, default=0.0),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(['question_id'], ['questions.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['characteristic_id'], ['characteristics.id'], onupdate='cascade', ondelete='set null'),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f('ix_answers_question_id'), 'answers', ['question_id'], unique=False)
    op.create_index(op.f('ix_answers_characteristic_id'), 'answers', ['characteristic_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_answers_question_id'), table_name='answers')
    op.drop_index(op.f('ix_answers_characteristic_id'), table_name='answers')
    op.drop_table('answers')
