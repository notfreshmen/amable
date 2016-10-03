from sqlalchemy import *
from migrate import *


meta = MetaData()
# Column('XXXX', String(120)),
posts = Table(
    'posts', meta,
    Column('id', Integer, primary_key=True),
    Column('text_brief', String(142), unique=False),
    Column('text_long', Text, unique=False),
    Column('answered', Boolean, unique=False),
    Column('hashtags', Text, unique=False),
    Column('image_url', String(128), unique=False),
    Column('user_id', Integer, unique=False),
    Column('community_id', Integer, unique=False),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    posts.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    posts.drop()
