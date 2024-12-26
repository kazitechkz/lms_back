"""add_course

Revision ID: fc6832372c77
Revises: 22a3c0af0c38
Create Date: 2024-12-26 16:45:15.853199

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fc6832372c77'
down_revision: Union[str, None] = '22a3c0af0c38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "courses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column("title_ru", sa.String(length=256), nullable=False),
        sa.Column("title_kk", sa.String(length=256), nullable=False),
        sa.Column("title_en", sa.String(length=256), nullable=True),
        sa.Column("short_description_kk", sa.Text(), nullable=False),
        sa.Column("short_description_ru", sa.Text(), nullable=False),
        sa.Column("short_description_en", sa.Text(), nullable=True),
        sa.Column("description_kk", sa.Text(), nullable=False),
        sa.Column("description_ru", sa.Text(), nullable=False),
        sa.Column("description_en", sa.Text(), nullable=True),
        sa.Column("learned_after_course_kk", sa.Text(), nullable=False),
        sa.Column("learned_after_course_ru", sa.Text(), nullable=False),
        sa.Column("learned_after_course_en", sa.Text(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("thumbnail", sa.String(length=256), nullable=True),
        sa.Column("author", sa.String(length=256), nullable=True),
        sa.ForeignKeyConstraint(['category_id'], ['course_categories.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['type_id'], ['course_types.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_courses_category_id'), 'courses', ['category_id'], unique=False)
    op.create_index(op.f('ix_courses_type_id'), 'courses', ['type_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_courses_category_id'), table_name='courses')
    op.drop_index(op.f('ix_courses_type_id'), table_name='courses')
    op.drop_table("tags")
