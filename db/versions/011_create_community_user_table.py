from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
community_users = Table(
    'community_users', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('community_id', Integer),
    Column('moderator', Boolean),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    community_users.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    community_users.drop()
