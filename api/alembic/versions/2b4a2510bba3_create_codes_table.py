"""Create codes table

Revision ID: 2b4a2510bba3
Revises: 8ac42d3270f5
Create Date: 2023-06-20 14:13:01.153994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b4a2510bba3'
down_revision = '8ac42d3270f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codes',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('ends_at', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('codes')
    # ### end Alembic commands ###
