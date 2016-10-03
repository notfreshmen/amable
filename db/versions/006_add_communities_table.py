from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
communitites = Table(
    'communitites', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(128), unique=False),
    Column('description', Text, unique=False),
    Column('banner_url', String(128), unique=False),
    Column('thumbnail_url', String(120), unique=False),
    Column('nsfw', Boolean, unique=False),
    Column('active', Boolean, unique=False),
    Column('num_upvotes', Integer, unique=False),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    communitites.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    communitites.drop()
