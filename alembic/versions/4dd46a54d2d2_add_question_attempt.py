"""add_question_attempt

Revision ID: 4dd46a54d2d2
Revises: fef9467c73f4
Create Date: 2025-01-08 11:57:02.890757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4dd46a54d2d2'
down_revision: Union[str, None] = 'fef9467c73f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'question_attempts',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("test_id", sa.Integer(), nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("answer_id", sa.Integer(), nullable=True),
        sa.Column("answer_ids", sa.JSON(), nullable=True),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("point", sa.Integer(), nullable=False),
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
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['test_id'], ['tests.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['question_id'], ['questions.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['answer_id'], ['answers.id'], onupdate='cascade', ondelete='cascade'),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f('ix_question_attempts_user_id'), 'question_attempts', ['user_id'], unique=False)
    op.create_index(op.f('ix_question_attempts_test_id'), 'question_attempts', ['test_id'], unique=False)
    op.create_index(op.f('ix_question_attempts_question_id'), 'question_attempts', ['question_id'], unique=False)
    op.create_index(op.f('ix_question_attempts_answer_id'), 'question_attempts', ['answer_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_question_attempts_user_id'), table_name='question_attempts')
    op.drop_index(op.f('ix_question_attempts_test_id'), table_name='question_attempts')
    op.drop_index(op.f('ix_question_attempts_question_id'), table_name='question_attempts')
    op.drop_index(op.f('ix_question_attempts_answer_id'), table_name='question_attempts')
    op.drop_table("question_attempts")
