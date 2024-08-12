"""create task model

Revision ID: cb1e52830bd2
Revises:
Create Date: 2024-07-12 11:56:51.993444

"""

from collections.abc import Sequence

import sqlalchemy as sa
import sqlmodel
import sqlmodel.sql.sqltypes
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cb1e52830bd2"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "task_status",
            sa.Enum("Initiated", "SSHConnected", "Failed", "Finished", name="taskstatus"),
            nullable=True,
        ),
        sa.Column("miner_hotkey", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("ssh_private_key", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task")
    # ### end Alembic commands ###