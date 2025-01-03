"""add_materials

Revision ID: fb39afe831a6
Revises: c6d38009546e
Create Date: 2025-01-03 11:23:48.206137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb39afe831a6'
down_revision: Union[str, None] = 'c6d38009546e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "materials",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['file_id'], ['files.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_materials_file_id'), 'materials', ['file_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_materials_file_id'), table_name='materials')
    op.drop_table("materials")
