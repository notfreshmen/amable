from sqlalchemy import *
from migrate import *


meta = MetaData()

post_reports = Table(
    'post_reports', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('post_id', Integer),
    Column('content', Text),
    Column('reason', String(64)),
    Column('resolved', Boolean),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    post_reports.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    post_reports.drop()
