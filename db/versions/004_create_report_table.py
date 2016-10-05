from sqlalchemy import *
from migrate import *


meta = MetaData()

reports = Table(
    'reports', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(80), unique=False),
    Column('content', String(120), unique=False),
    Column('user_id', Integer, unique=False),
    Column('category', String(120), unique=False),
    Column('resolved', Boolean, unique=False),
    Column('date_created', DateTime, unique=False),
    Column('date_modified', DateTime, unique=False)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    reports.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    reports.drop()
