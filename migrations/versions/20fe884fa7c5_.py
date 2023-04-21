"""empty message

Revision ID: 20fe884fa7c5
Revises: 2da4d62aee74
Create Date: 2023-04-21 13:52:48.994096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20fe884fa7c5'
down_revision = '2da4d62aee74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empresas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descripcion', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empresas', schema=None) as batch_op:
        batch_op.drop_column('descripcion')

    # ### end Alembic commands ###
