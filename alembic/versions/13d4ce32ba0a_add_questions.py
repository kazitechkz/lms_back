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
        "question_types",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title_ru", sa.String(length=256), nullable=False),
        sa.Column("title_kk", sa.String(length=256), nullable=False),
        sa.Column("title_en", sa.String(length=256), nullable=True),
        sa.Column("value", sa.String(length=256), nullable=False),
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
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('test_id', sa.Integer, nullable=False),
        sa.Column('text', sa.Text, nullable=False),
        sa.Column('hint', sa.Text, nullable=True),
        sa.Column('explanation', sa.Text, nullable=True),
        sa.Column('type_id', sa.Integer, nullable=False),
        sa.Column('points', sa.Float, default=1.0),
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
        sa.ForeignKeyConstraint(['test_id'], ['tests.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['type_id'], ['test_types.id'], onupdate='cascade', ondelete='cascade'),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f('ix_questions_test_id'), 'questions', ['test_id'], unique=False)
    op.create_index(op.f('ix_questions_type_id'), 'questions', ['type_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_questions_test_id'), table_name='questions')
    op.drop_index(op.f('ix_questions_type_id'), table_name='questions')
    op.drop_table('question_types')
    op.drop_table('questions')
