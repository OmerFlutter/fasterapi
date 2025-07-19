"""create posts table

Revision ID: a0382fdea83c
Revises: 
Create Date: 2025-07-15 14:10:29.511621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0382fdea83c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column('id', sa.Integer, primary_key=True, nullable=False), 
        sa.Column('title', sa.String, nullable=False),
        sa.Column('content',sa.String, nullable=False),
        sa.Column('published', sa.Boolean, server_default='TRUE', nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
        )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
