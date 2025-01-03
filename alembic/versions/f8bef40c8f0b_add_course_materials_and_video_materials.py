"""add course_materials and video_materials

Revision ID: f8bef40c8f0b
Revises: fb39afe831a6
Create Date: 2025-01-03 11:26:46.002439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8bef40c8f0b'
down_revision: Union[str, None] = 'fb39afe831a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "course_materials",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("course_id", sa.Integer(), nullable=False),
        sa.Column('material_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['material_id'], ['materials.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_course_materials_course_id'), 'course_materials', ['course_id'], unique=False)
    op.create_index(op.f('ix_course_materials_material_id'), 'course_materials', ['material_id'], unique=False)

    op.create_table(
        "video_materials",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("video_id", sa.Integer(), nullable=False),
        sa.Column('material_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['video_id'], ['video_courses.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['material_id'], ['materials.id'], onupdate='cascade', ondelete='cascade'),
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
    op.create_index(op.f('ix_video_materials_video_id'), 'video_materials', ['video_id'], unique=False)
    op.create_index(op.f('ix_video_materials_material_id'), 'video_materials', ['material_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_course_materials_course_id'), table_name='course_materials')
    op.drop_index(op.f('ix_course_materials_material_id'), table_name='course_materials')
    op.drop_table("course_materials")

    op.drop_index(op.f('ix_video_materials_video_id'), table_name='video_materials')
    op.drop_index(op.f('ix_video_materials_material_id'), table_name='video_materials')
    op.drop_table("video_materials")
