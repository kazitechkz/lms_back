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
        'feedbacks',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('test_id', sa.Integer, nullable=False),
        sa.Column('question_id', sa.Integer, nullable=True),
        sa.Column('description', sa.Text, nullable=False),
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
        sa.ForeignKeyConstraint(['question_id'], ['questions.id'], onupdate='cascade', ondelete='set null'),
        sa.PrimaryKeyConstraint("id")

    )
    op.create_index(op.f('ix_feedbacks_test_id'), 'feedbacks', ['test_id'], unique=False)
    op.create_index(op.f('ix_feedbacks_question_id'), 'feedbacks', ['question_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_feedbacks_test_id'), table_name='feedbacks')
    op.drop_index(op.f('ix_feedbacks_question_id'), table_name='feedbacks')
    op.drop_table('feedbacks')
