from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    AAAA = Table('AAAA', meta, autoload=True)
    BBBB = Table('BBBB', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[AAAA.c.XXXX],
        refcolumns=[BBBB.c.XXXX]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    AAAA = Table('AAAA', meta, autoload=True)
    BBBB = Table('BBBB', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[AAAA.c.XXXX],
        refcolumns=[BBBB.c.XXXX]).drop()
    pass
