"""Old version IVR log

Revision ID: 5af1f502ac5c
Revises: f59883bf2bc1
Create Date: 2018-03-17 06:30:56.852305

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "5af1f502ac5c"
down_revision = "f59883bf2bc1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("ivrlog")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ivrlog",
        sa.Column("log_id", mysql.VARCHAR(length=80), nullable=False),
        sa.Column("log_dtime", mysql.DATETIME(), nullable=True),
        sa.Column("group_id", mysql.VARCHAR(length=12), nullable=False),
        sa.Column("member_id", mysql.VARCHAR(length=45), nullable=False),
        sa.Column("item_id", mysql.VARCHAR(length=12), nullable=False),
        sa.ForeignKeyConstraint(
            ["group_id", "member_id"],
            ["member.group_id", "member.member_id"],
            name="fk_ivrlog_group_id_member",
        ),
        sa.ForeignKeyConstraint(
            ["item_id"], ["menuitem.item_id"], name="fk_ivrlog_item_id_menuitem"
        ),
        sa.PrimaryKeyConstraint("log_id"),
        mysql_default_charset="latin1",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###
