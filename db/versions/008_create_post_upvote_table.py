from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
post_upvote = Table(
    'post_upvotes', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, unique=False),
    Column('post_id', Integer, unique=False),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    post_upvote.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    post_upvote.drop()
