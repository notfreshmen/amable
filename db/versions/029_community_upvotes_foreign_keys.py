from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    communities = Table('communities', meta, autoload=True)
    community_upvotes = Table('community_upvotes', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[community_upvotes.c.user_id],
        refcolumns=[users.c.id]).create()

    ForeignKeyConstraint(
        columns=[community_upvotes.c.community_id],
        refcolumns=[communities.c.id]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    communities = Table('communities', meta, autoload=True)
    community_upvotes = Table('community_upvotes', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[community_upvotes.c.user_id],
        refcolumns=[users.c.id]).drop()

    ForeignKeyConstraint(
        columns=[community_upvotes.c.community_id],
        refcolumns=[communities.c.id]).drop()
    pass
