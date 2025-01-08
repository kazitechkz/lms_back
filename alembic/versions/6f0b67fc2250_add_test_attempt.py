"""add_test_attempt

Revision ID: 6f0b67fc2250
Revises: 4dd46a54d2d2
Create Date: 2025-01-08 17:01:32.954404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f0b67fc2250'
down_revision: Union[str, None] = '4dd46a54d2d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'test_attempts',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("test_id", sa.Integer(), nullable=False),
        sa.Column("is_success", sa.Boolean(), nullable=False),
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
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f('ix_question_attempts_user_id'), 'test_attempts', ['user_id'], unique=False)
    op.create_index(op.f('ix_question_attempts_test_id'), 'test_attempts', ['test_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_question_attempts_user_id'), table_name='question_attempts')
    op.drop_index(op.f('ix_question_attempts_test_id'), table_name='question_attempts')
    op.drop_table("test_attempts")
