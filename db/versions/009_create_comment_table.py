from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
comments = Table(
    'comments', meta,
    Column('id', Integer, primary_key=True),
    Column('content', Text, unique=False),
    Column('hashtags', Text, unique=False),
    Column('parent', Integer, unique=False, nullable=True),
    Column('user_id', Integer),
    Column('post_id', Integer),
    Column('upvote_count', String(128), unique=False),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    comments.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    comments.drop()
