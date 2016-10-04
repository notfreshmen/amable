from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    post_upvotes = Table('post_upvotes', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[post_upvotes.c.user_id],
        refcolumns=[users.c.id]).create()

    ForeignKeyConstraint(
        columns=[post_upvotes.c.post_id],
        refcolumns=[posts.c.id]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    post_upvotes = Table('post_upvotes', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[post_upvotes.c.user_id],
        refcolumns=[users.c.id]).drop()

    ForeignKeyConstraint(
        columns=[post_upvotes.c.post_id],
        refcolumns=[posts.c.id]).drop()
    pass
