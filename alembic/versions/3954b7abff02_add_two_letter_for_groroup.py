"""Add two letter for groroup

Revision ID: 3954b7abff02
Revises: f1c502e88145
Create Date: 2018-07-12 11:28:59.724361

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3954b7abff02"
down_revision = "f1c502e88145"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "advgroup", sa.Column("group_twoword", sa.String(length=3), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("advgroup", "group_twoword")
    # ### end Alembic commands ###
