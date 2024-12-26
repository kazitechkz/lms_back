"""add_course_tag

Revision ID: 67ad9174bd78
Revises: fc6832372c77
Create Date: 2024-12-26 17:21:54.601750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67ad9174bd78'
down_revision: Union[str, None] = 'fc6832372c77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "course_tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_courses_course_id'), 'course_tags', ['course_id'], unique=False)
    op.create_index(op.f('ix_courses_tag_id'), 'course_tags', ['tag_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_courses_course_id'), table_name='course_tags')
    op.drop_index(op.f('ix_courses_tag_id'), table_name='course_tags')
    op.drop_table("course_tags")
