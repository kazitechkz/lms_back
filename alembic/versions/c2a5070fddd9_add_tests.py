"""add_tests

Revision ID: c2a5070fddd9
Revises: e43b193eb74d
Create Date: 2025-01-03 16:18:27.588599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2a5070fddd9'
down_revision: Union[str, None] = 'e43b193eb74d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'test_types',
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
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        'tests',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=256), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('is_demo', sa.Boolean(), default=False),
        sa.Column('organization_id', sa.Integer(), nullable=True),
        sa.Column('course_id', sa.Integer(), nullable=True),
        sa.Column('video_id', sa.Integer(), nullable=True),
        sa.Column('time_limit', sa.Integer(), nullable=True),
        sa.Column('pass_point', sa.Integer(), nullable=True),
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
        sa.ForeignKeyConstraint(['type_id'], ['test_types.id'], onupdate='cascade', ondelete='cascade'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], onupdate='cascade', ondelete='set null'),
        sa.ForeignKeyConstraint(['video_id'], ['video_courses.id'], onupdate='cascade', ondelete='set null'),
        sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], onupdate='cascade', ondelete='set null'),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f('ix_tests_type_id'), 'tests', ['type_id'], unique=False)
    op.create_index(op.f('ix_tests_video_id'), 'tests', ['video_id'], unique=False)
    op.create_index(op.f('ix_tests_course_id'), 'tests', ['course_id'], unique=False)
    op.create_index(op.f('ix_tests_organization_id'), 'tests', ['organization_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_tests_type_id'), table_name='tests')
    op.drop_index(op.f('ix_tests_video_id'), table_name='tests')
    op.drop_index(op.f('ix_tests_course_id'), table_name='tests')
    op.drop_index(op.f('ix_tests_organization_id'), table_name='tests')
    op.drop_table('test_types')
    op.drop_table('tests')
