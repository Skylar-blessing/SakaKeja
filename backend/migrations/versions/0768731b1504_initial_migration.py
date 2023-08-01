"""initial migration

Revision ID: 0768731b1504
Revises: 
Create Date: 2023-07-31 11:49:56.142725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0768731b1504'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('user_type', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('move_assistance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_details', sa.String(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tenant_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('number_of_rooms', sa.Integer(), nullable=True),
    sa.Column('categories', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('image_urls', sa.ARRAY(sa.String()), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('payment_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], ),
    sa.ForeignKeyConstraint(['tenant_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_text', sa.String(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], ),
    sa.ForeignKeyConstraint(['tenant_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('payments')
    op.drop_table('properties')
    op.drop_table('move_assistance')
    op.drop_table('users')
    # ### end Alembic commands ###
