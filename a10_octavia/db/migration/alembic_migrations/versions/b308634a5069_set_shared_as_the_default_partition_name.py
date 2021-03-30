"""Set 'shared' as the default partition name

Revision ID: b308634a5069
Revises: 34a0d811941d
Create Date: 2021-03-30 23:42:36.559792

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b308634a5069'
down_revision = '34a0d811941d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('nat_pool', 'member_ref_count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('vrid', 'vrid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('vrid', 'vrid_floating_ip',
               existing_type=mysql.VARCHAR(length=40),
               nullable=True)
    op.alter_column('vthunders', 'hierarchical_multitenancy',
               existing_type=mysql.VARCHAR(length=7),
               nullable=False)
    op.alter_column('vthunders', 'last_udp_update',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('vthunders', 'partition_name',
               existing_type=mysql.VARCHAR(length=14),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vthunders', 'partition_name',
               existing_type=mysql.VARCHAR(length=14),
               nullable=True)
    op.alter_column('vthunders', 'last_udp_update',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('vthunders', 'hierarchical_multitenancy',
               existing_type=mysql.VARCHAR(length=7),
               nullable=True)
    op.alter_column('vrid', 'vrid_floating_ip',
               existing_type=mysql.VARCHAR(length=40),
               nullable=False)
    op.alter_column('vrid', 'vrid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('nat_pool', 'member_ref_count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
