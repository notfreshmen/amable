from sqlalchemy import *
from migrate import *


parent_id_column = Column('parent_id', Integer)


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    reports = Table('reports', meta, autoload=True)

    parent_id_column.create(reports)


def downgrade(migrate_engine):
    parent_id_column.drop()
