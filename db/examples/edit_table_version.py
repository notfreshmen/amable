from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    XXXX = Table('XXXX', meta, autoload=True)

    # password = Column("password", String(128), nullable=False)
    XXXX = Column("XXXX", String(128), nullable=False)
    XXXX = Column("XXXX", String(128), nullable=False)

    # password.create(users)
    XXXX.create(users)
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    XXXX = Table('XXXX', meta, autoload=True)

    # users.c.password.drop()
    XXXX.c.XXXX.drop()
    pass
