"""empty message

Revision ID: e8dd466cf442
Revises: 
Create Date: 2023-07-27 10:10:28.626444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e8dd466cf442'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Drop the foreign key constraints
    op.drop_constraint('owners_tenants_owner_id_fkey', 'owners_tenants', type_='foreignkey')
    op.drop_constraint('tenants_houses_house_id_fkey', 'tenants_houses', type_='foreignkey')
    op.drop_constraint('owners_tenants_tenant_id_fkey', 'owners_tenants', type_='foreignkey')
    op.drop_constraint('tenants_houses_tenant_id_fkey', 'tenants_houses', type_='foreignkey')
    op.drop_constraint('reviews_house_id_fkey', 'reviews', type_='foreignkey')

    # Drop the tables
    op.drop_table('houses')
    op.drop_table('reviews')
    op.drop_table('tenants')
    op.drop_table('owners')
    op.drop_table('tenants_houses')
    op.drop_table('owners_tenants')
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # Create the tables
    op.create_table('owners',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('owners_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='owners_pkey'),
    sa.UniqueConstraint('email', name='owners_email_key'),
    postgresql_ignore_search_path=False
    )
    
    op.create_table('tenants',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('tenants_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='tenants_pkey'),
    sa.UniqueConstraint('email', name='tenants_email_key'),
    postgresql_ignore_search_path=False
    )
    
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('reviews', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('house_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tenant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['houses.id'], name='reviews_house_id_fkey'),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='reviews_tenant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    
    op.create_table('houses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('number_of_rooms', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('categories', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('image_urls', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tenant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name='houses_owner_id_fkey'),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='houses_tenant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='houses_pkey')
    )

    op.create_table('tenants_houses',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('tenant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('house_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['houses.id'], name='tenants_houses_house_id_fkey'),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='tenants_houses_tenant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tenants_houses_pkey')
    )

    op.create_table('owners_tenants',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tenant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name='owners_tenants_owner_id_fkey'),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='owners_tenants_tenant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='owners_tenants_pkey')
    )
    # ### end Alembic commands ###
