"""create users table

Revision ID: 6306f161f8be
Revises: a0382fdea83c
Create Date: 2025-07-15 14:24:29.431640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6306f161f8be'
down_revision: Union[str, Sequence[str], None] = 'a0382fdea83c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column('id', sa.Integer, primary_key=True, nullable=False), 
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password',sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
        )
    pass

def downgrade() -> None:
    op.drop_table("users")
    pass
