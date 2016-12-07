from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
followers = Table(
    'followers', meta,
    Column('source_id', Integer, primary_key=True),
    Column('target_id', Integer, primary_key=True),
    Column('date_created', DateTime),
    Column('date_modified', DateTime)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    followers.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    followers.drop()
