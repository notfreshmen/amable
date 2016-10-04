from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[comments.c.user_id],
        refcolumns=[users.c.id]).create()

    ForeignKeyConstraint(
        columns=[comments.c.post_id],
        refcolumns=[posts.c.id]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[comments.c.user_id],
        refcolumns=[users.c.id]).drop()

    ForeignKeyConstraint(
        columns=[comments.c.post_id],
        refcolumns=[posts.c.id]).drop()
    pass
