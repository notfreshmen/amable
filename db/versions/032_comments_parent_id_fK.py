from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[comments.c.parent_id],
        refcolumns=[comments.c.id]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[comments.c.parent_id],
        refcolumns=[comments.c.id]).drop()
    pass
