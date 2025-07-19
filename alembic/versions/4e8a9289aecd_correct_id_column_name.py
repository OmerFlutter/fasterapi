"""correct id column name

Revision ID: 4e8a9289aecd
Revises: 6306f161f8be
Create Date: 2025-07-17 14:24:18.107170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e8a9289aecd'
down_revision: Union[str, Sequence[str], None] = '6306f161f8be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "posts",
        column_name='ids',
        new_column_name='id',
        )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
