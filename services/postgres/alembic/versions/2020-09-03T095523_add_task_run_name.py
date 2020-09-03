"""
Add task run name

Revision ID: e148cf9f1e5b
Revises: c1f317aa658c
Create Date: 2020-09-03 09:55:23.155317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID


# revision identifiers, used by Alembic.
revision = "e148cf9f1e5b"
down_revision = "c1f317aa658c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("task_run", sa.Column("name", sa.String))


def downgrade():
    op.drop_column("task_run", "name")
