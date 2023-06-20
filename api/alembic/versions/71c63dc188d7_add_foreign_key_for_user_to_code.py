"""Add foreign key for user to code

Revision ID: 71c63dc188d7
Revises: 2b4a2510bba3
Create Date: 2023-06-20 14:35:53.524695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71c63dc188d7'
down_revision = '2b4a2510bba3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('codes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'codes', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'codes', type_='foreignkey')
    op.drop_column('codes', 'user_id')
    # ### end Alembic commands ###
