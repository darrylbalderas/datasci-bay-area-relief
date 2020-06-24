"""empty message

Revision ID: 6ad204012c61
Revises: 
Create Date: 2020-06-18 09:27:35.671683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ad204012c61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relief',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sf_county', sa.Enum('yes', 'no', 'unknown', name='uniquecountyenum'), nullable=True),
    sa.Column('alameda_county', sa.Enum('yes', 'no', 'unknown', name='uniquecountyenum'), nullable=True),
    sa.Column('san_mateo_county', sa.Enum('yes', 'no', 'unknown', name='uniquecountyenum'), nullable=True),
    sa.Column('contra_costa_county', sa.Enum('yes', 'no', 'unknown', name='uniquecountyenum'), nullable=True),
    sa.Column('santa_clara_county', sa.Enum('yes', 'no', 'unknown', name='uniquecountyenum'), nullable=True),
    sa.Column('county', sa.Enum('all', 'some', 'unknown', name='countyenum'), nullable=True),
    sa.Column('category', sa.Enum('agriculture', 'all', 'unknown', 'multiple', 'healthcare', 'entertainment', 'hospitality', 'manufacturing', 'education', 'mass_media', 'software', 'real_estate', 'sport', 'transport', 'financial', name='categoryenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relief')
    # ### end Alembic commands ###