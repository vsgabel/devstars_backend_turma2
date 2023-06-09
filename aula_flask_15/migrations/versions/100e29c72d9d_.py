"""empty message

Revision ID: 100e29c72d9d
Revises: e0c61c6f3daa
Create Date: 2023-04-11 19:58:29.006663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '100e29c72d9d'
down_revision = 'e0c61c6f3daa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha_hash', sa.String(length=128), nullable=False))
        batch_op.drop_column('senha')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', mysql.VARCHAR(length=128), nullable=False))
        batch_op.drop_column('senha_hash')

    # ### end Alembic commands ###
