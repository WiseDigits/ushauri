"""Add name and start to items

Revision ID: d65450476091
Revises: 41e14ace132a
Create Date: 2018-03-17 08:38:16.175107

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "d65450476091"
down_revision = "41e14ace132a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "menuitem", sa.Column("item_name", sa.String(length=120), nullable=True)
    )
    op.add_column("menuitem", sa.Column("item_start", sa.Integer(), nullable=True))
    op.drop_column("menuitem", "item_pos")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "menuitem",
        sa.Column(
            "item_pos",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("menuitem", "item_start")
    op.drop_column("menuitem", "item_name")
    # ### end Alembic commands ###
