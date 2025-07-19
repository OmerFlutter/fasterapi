"""empty message

Revision ID: f0b17c55384d
Revises: 3129e0d357f8
Create Date: 2025-07-18 13:41:53.563261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0b17c55384d'
down_revision: Union[str, Sequence[str], None] = '3129e0d357f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
