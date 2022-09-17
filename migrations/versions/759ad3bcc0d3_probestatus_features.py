"""ProbeStatus Features

Revision ID: 759ad3bcc0d3
Revises: 9cea40c99d9b
Create Date: 2021-04-28 11:35:29.159850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '759ad3bcc0d3'
down_revision = '9cea40c99d9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('probe_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('probe_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Text(), nullable=False),
    sa.Column('begin', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['probe_id'], ['probe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_probe_status_active'), 'probe_status', ['active'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_probe_status_active'), table_name='probe_status')
    op.drop_table('probe_status')
    # ### end Alembic commands ###
