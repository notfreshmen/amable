from sqlalchemy import *
from migrate import *


meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(80), unique=True),
    Column('email', String(120), unique=True)
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    users.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    users.drop()
