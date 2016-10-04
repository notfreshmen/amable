from sqlalchemy import *
from migrate import *


type_column = Column('type', String(20))


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    reports = Table('reports', meta, autoload=True)

    type_column.create(reports)


def downgrade(migrate_engine):
    type_column.drop()
