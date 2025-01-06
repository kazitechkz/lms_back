"""add_blogs

Revision ID: fef9467c73f4
Revises: 53cccb620123
Create Date: 2025-01-06 13:17:43.263774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fef9467c73f4'
down_revision: Union[str, None] = '53cccb620123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'blog_categories',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
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
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("short_description", sa.Text(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("thumbnail", sa.Text(), nullable=True),
        sa.Column("author", sa.String(length=256), nullable=True),
        sa.Column("status", sa.Boolean(), nullable=False),
        sa.Column("lang_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=True),
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
        sa.ForeignKeyConstraint(['lang_id'], ['languages.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['category_id'], ['blog_categories.id'], onupdate='cascade', ondelete='set null'),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f('ix_blogs_lang_id'), 'blogs', ['lang_id'], unique=False)
    op.create_index(op.f('ix_blogs_category_id'), 'blogs', ['category_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_blogs_lang_id'), table_name='blogs')
    op.drop_index(op.f('ix_blogs_category_id'), table_name='blogs')
    op.drop_table("blog_categories")
    op.drop_table("blogs")
