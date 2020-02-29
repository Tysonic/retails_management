"""empty message

Revision ID: 952a2d1bb485
Revises: 
Create Date: 2020-01-27 20:24:58.509679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952a2d1bb485'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Debtors',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('debtor', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('ItemBrands',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('ItemNames',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_index(op.f('ix_ItemNames__Id'), 'ItemNames', ['_Id'], unique=False)
    op.create_table('ItemPackaging',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('packaging', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('ItemUnits',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('unit', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('Profiles',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('other_name', sa.String(), nullable=True),
    sa.Column('home_address', sa.String(), nullable=True),
    sa.Column('next_of_kin', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('telephone_contact', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('State',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('states', sa.String(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('_Id'),
    sa.UniqueConstraint('states')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=True)
    op.create_index(op.f('ix_Users_id'), 'Users', ['id'], unique=False)
    op.create_index(op.f('ix_Users_username'), 'Users', ['username'], unique=True)
    op.create_table('Images',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('uploaded_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['status'], ['State._Id'], ),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('Items',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('brand', sa.Integer(), nullable=True),
    sa.Column('unit', sa.Integer(), nullable=True),
    sa.Column('packaging', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['brand'], ['ItemBrands._Id'], ),
    sa.ForeignKeyConstraint(['name'], ['ItemNames._Id'], ),
    sa.ForeignKeyConstraint(['packaging'], ['ItemPackaging._Id'], ),
    sa.ForeignKeyConstraint(['unit'], ['ItemUnits._Id'], ),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_index(op.f('ix_Items__Id'), 'Items', ['_Id'], unique=False)
    op.create_table('debt_repayment',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('debt', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('repaid_by', sa.String(), nullable=True),
    sa.Column('repaid_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['debt'], ['Debtors._Id'], ),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_index(op.f('ix_debt_repayment__Id'), 'debt_repayment', ['_Id'], unique=False)
    op.create_table('expenses',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('reason', sa.String(), nullable=True),
    sa.Column('details', sa.String(), nullable=True),
    sa.Column('issued_by', sa.Integer(), nullable=True),
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['issued_by'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_index(op.f('ix_expenses__Id'), 'expenses', ['_Id'], unique=False)
    op.create_table('Purchases',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.Date(), nullable=True),
    sa.Column('recorded_at', sa.DateTime(), nullable=True),
    sa.Column('purchased_by', sa.String(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('quantity_purchased', sa.Integer(), nullable=False),
    sa.Column('item_purchased', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_purchased'], ['Items._Id'], ),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_table('Sales',
    sa.Column('_Id', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('quantity_sold', sa.Integer(), nullable=False),
    sa.Column('sold_by', sa.String(), nullable=True),
    sa.Column('sold_on', sa.DateTime(), nullable=True),
    sa.Column('recorded_at', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('item_sold', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_sold'], ['Items._Id'], ),
    sa.PrimaryKeyConstraint('_Id')
    )
    op.create_index(op.f('ix_Sales__Id'), 'Sales', ['_Id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Sales__Id'), table_name='Sales')
    op.drop_table('Sales')
    op.drop_table('Purchases')
    op.drop_index(op.f('ix_expenses__Id'), table_name='expenses')
    op.drop_table('expenses')
    op.drop_index(op.f('ix_debt_repayment__Id'), table_name='debt_repayment')
    op.drop_table('debt_repayment')
    op.drop_index(op.f('ix_Items__Id'), table_name='Items')
    op.drop_table('Items')
    op.drop_table('Images')
    op.drop_index(op.f('ix_Users_username'), table_name='Users')
    op.drop_index(op.f('ix_Users_id'), table_name='Users')
    op.drop_index(op.f('ix_Users_email'), table_name='Users')
    op.drop_table('Users')
    op.drop_table('State')
    op.drop_table('Profiles')
    op.drop_table('ItemUnits')
    op.drop_table('ItemPackaging')
    op.drop_index(op.f('ix_ItemNames__Id'), table_name='ItemNames')
    op.drop_table('ItemNames')
    op.drop_table('ItemBrands')
    op.drop_table('Debtors')
    # ### end Alembic commands ###
