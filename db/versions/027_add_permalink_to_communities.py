from sqlalchemy import *
from migrate import *


permalink_column = Column('permalink', String(128))


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    communities = Table('communities', meta, autoload=True)

    permalink_column.create(communities)


def downgrade(migrate_engine):
    permalink_column.drop()
