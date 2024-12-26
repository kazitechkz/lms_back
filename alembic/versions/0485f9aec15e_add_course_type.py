"""Add CategoryModel

Revision ID: 0485f9aec15e
Revises: 56978bf0207f
Create Date: 2024-12-26 10:44:40.819566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0485f9aec15e'
down_revision: Union[str, None] = '56978bf0207f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "course_types",
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
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("course_types")
