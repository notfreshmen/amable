from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
hashtag = Table(
    'hashtags', meta,
    Column('id', Integer, primary_key=True),
    Column('tag', String(128), unique=False),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    hashtag.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    hashtag.drop()
