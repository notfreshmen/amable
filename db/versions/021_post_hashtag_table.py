from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
post_hashtag = Table(
    'post_hashtags', meta,
    Column('post_id', Integer, primary_key=True),
    Column('hashtag_id', Integer, primary_key=True),
    Column('date_created', DateTime),
    Column('date_modified', DateTime)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    post_hashtag.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    post_hashtag.drop()
