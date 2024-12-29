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
        sa.Column('lang_id', sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("short_description", sa.Text(), nullable=True),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("learned", sa.Text(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("thumbnail", sa.String(length=256), nullable=True),
        sa.Column("author", sa.String(length=256), nullable=True),
        sa.ForeignKeyConstraint(['lang_id'], ['languages.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_courses_lang_id'), 'courses', ['lang_id'], unique=False)
    op.create_index(op.f('ix_courses_category_id'), 'courses', ['category_id'], unique=False)
    op.create_index(op.f('ix_courses_type_id'), 'courses', ['type_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_courses_lang_id'), table_name='courses')
    op.drop_index(op.f('ix_courses_category_id'), table_name='courses')
    op.drop_index(op.f('ix_courses_type_id'), table_name='courses')
    op.drop_table("courses")
