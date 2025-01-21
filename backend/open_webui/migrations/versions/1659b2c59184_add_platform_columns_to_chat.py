"""Add platform columns to chat

Revision ID: 1659b2c59184
Revises: 3781e22d8b01
Create Date: 2025-01-21 11:52:53.937853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "1659b2c59184"
down_revision: Union[str, None] = "3781e22d8b01"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("chat", sa.Column("platform_key", sa.Text(), nullable=True))
    op.add_column("chat", sa.Column("platform_id", sa.BigInteger(), nullable=True))


def downgrade() -> None:
    op.drop_column("chat", "platform_id")
    op.drop_column("chat", "platform_key")
