"""add_video_courses

Revision ID: 4cf9d6881125
Revises: 67ad9174bd78
Create Date: 2024-12-30 11:17:51.656069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cf9d6881125'
down_revision: Union[str, None] = '67ad9174bd78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "video_courses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.Column('lang_id', sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=256), nullable=False),
        sa.Column("video_id", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("image", sa.Text(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("is_first", sa.Boolean(), nullable=False),
        sa.Column("is_last", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['video_id'], ['files.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['lang_id'], ['languages.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_video_courses_course_id'), 'video_courses', ['course_id'], unique=False)
    op.create_index(op.f('ix_video_courses_video_id'), 'video_courses', ['video_id'], unique=False)
    op.create_index(op.f('ix_video_courses_lang_id'), 'video_courses', ['lang_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_video_courses_course_id'), table_name='video_courses')
    op.drop_index(op.f('ix_video_courses_video_id'), table_name='video_courses')
    op.drop_index(op.f('ix_video_courses_lang_id'), table_name='video_courses')
    op.drop_table("video_courses")
