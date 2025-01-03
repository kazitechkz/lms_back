"""add_characteristics

Revision ID: 37e227e9d6fa
Revises: 13d4ce32ba0a
Create Date: 2025-01-03 16:20:27.716026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37e227e9d6fa'
down_revision: Union[str, None] = '13d4ce32ba0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'characteristics',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title_kk', sa.String(length=256), nullable=False),
        sa.Column('title_ru', sa.String(length=256), nullable=False),
        sa.Column('title_en', sa.String(length=256), nullable=True),
        sa.Column('description_kk', sa.Text, nullable=True),
        sa.Column('description_ru', sa.Text, nullable=True),
        sa.Column('description_en', sa.Text, nullable=True),
        sa.Column('value', sa.String(length=256), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('characteristics')
