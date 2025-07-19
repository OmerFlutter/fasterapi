"""create foreign key in posts

Revision ID: 11f356e8344a
Revises: f0b17c55384d
Create Date: 2025-07-18 13:46:51.963680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11f356e8344a'
down_revision: Union[str, Sequence[str], None] = 'f0b17c55384d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("creator_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "fk_posts_creator_id_users",
        "posts",  # source table
        "users",  # referent table
        ["creator_id"],  # source column
        ["id"],  # referent column
        ondelete="CASCADE"  # action on delete
    )
    pass


def downgrade() -> None:
    op.drop_constraint("fk_posts_creator_id_users", table_name="posts")
    op.drop_column("posts", "creator_id")
    pass
