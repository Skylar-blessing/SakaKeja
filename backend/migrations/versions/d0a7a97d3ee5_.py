"""empty message

Revision ID: d0a7a97d3ee5
Revises: 0d8346de73f5
Create Date: 2023-07-31 12:24:32.500498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a7a97d3ee5'
down_revision = '0d8346de73f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('move_assistance', schema=None) as batch_op:
        batch_op.alter_column('tenant_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('move_assistance', schema=None) as batch_op:
        batch_op.alter_column('tenant_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###