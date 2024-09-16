"""lol

Revision ID: 166a3d4a8c9a
Revises: beb1fd3f3aea
Create Date: 2024-08-19 14:23:11.912608

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '166a3d4a8c9a'
down_revision = 'beb1fd3f3aea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mois')
    with op.batch_alter_table('designation_journaliere', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mois', sa.String(length=10), nullable=False))
        batch_op.drop_constraint('designation_journaliere_ibfk_2', type_='foreignkey')
        batch_op.drop_column('mois_id')

    with op.batch_alter_table('vente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mois', sa.String(length=10), nullable=False))
        batch_op.drop_constraint('vente_ibfk_4', type_='foreignkey')
        batch_op.drop_column('mois_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mois_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('vente_ibfk_4', 'mois', ['mois_id'], ['id'])
        batch_op.drop_column('mois')

    with op.batch_alter_table('designation_journaliere', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mois_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('designation_journaliere_ibfk_2', 'mois', ['mois_id'], ['id'])
        batch_op.drop_column('mois')

    op.create_table('mois',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('libelle', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('travail', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vente', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
