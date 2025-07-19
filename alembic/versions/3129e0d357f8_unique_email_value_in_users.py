"""unique email value in users

Revision ID: 3129e0d357f8
Revises: 4e8a9289aecd
Create Date: 2025-07-17 14:26:38.467995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3129e0d357f8'
down_revision: Union[str, Sequence[str], None] = '4e8a9289aecd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        column_name='email',
        existing_type=sa.String(),
        nullable=False,
        existing_nullable=True,
        unique=True,    
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
