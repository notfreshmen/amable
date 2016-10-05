from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
XXXX = Table(
    'XXXX', meta,
    Column('id', Integer, primary_key=True),
    Column('XXXX', String(80)),
    Column('XXXX', String(128)),
    Column('date_created', DateTime),
    Column('date_modified', DateTime)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    XXXX.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    XXXX.drop()
