from sqlalchemy import *
from migrate import *


meta = MetaData()
comment_hashtag = Table(
    'comment_hashtags', meta,
    Column('comment_id', Integer, primary_key=True),
    Column('hashtag_id', Integer, primary_key=True),
    Column('date_created', DateTime),
    Column('date_modified', DateTime)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    comment_hashtag.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    comment_hashtag.drop()
