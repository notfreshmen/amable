from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
community_upvotes = Table(
    'community_upvotes', meta,
    Column('user_id', Integer, primary_key=True),
    Column('community_id', Integer, primary_key=True),
    Column('date_created', DateTime),
    Column('date_modified', DateTime)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    community_upvotes.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    community_upvotes.drop()
