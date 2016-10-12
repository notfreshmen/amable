from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    post_hashtags = Table('post_hashtags', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)
    hashtags = Table('hashtags', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[post_hashtags.c.hashtag_id],
        refcolumns=[hashtags.c.id]).create()

    ForeignKeyConstraint(
        columns=[post_hashtags.c.post_id],
        refcolumns=[posts.c.id]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # hashtags = Table('hashtags', meta, autoload=True)
    post_hashtags = Table('post_hashtags', meta, autoload=True)
    hashtags = Table('hashtags', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[post_hashtags.c.user_id],
        refcolumns=[hashtags.c.id]).drop()

    ForeignKeyConstraint(
        columns=[post_hashtags.c.post_id],
        refcolumns=[posts.c.id]).drop()
    pass
