from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    users = Table('users', meta, autoload=True)

    # password = Column("password", String(128), nullable=False)
    active = Column("active", Boolean)

    # password.create(users)
    active.create(users)
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    users = Table('users', meta, autoload=True)

    # users.c.password.drop()
    users.c.active.drop()
    pass
