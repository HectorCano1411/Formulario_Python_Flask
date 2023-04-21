"""empty message

Revision ID: 2da4d62aee74
Revises: f13340260263
Create Date: 2023-04-15 00:19:15.050395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2da4d62aee74'
down_revision = 'f13340260263'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empresas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('telefono', sa.Integer(), nullable=True),
    sa.Column('comuna', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('categoria', sa.String(length=250), nullable=True),
    sa.Column('producto_o_servicio', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empresas')
    # ### end Alembic commands ###