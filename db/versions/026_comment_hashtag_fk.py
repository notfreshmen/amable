from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    comment_hashtags = Table('comment_hashtags', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)
    hashtags = Table('hashtags', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[comment_hashtags.c.hashtag_id],
        refcolumns=[hashtags.c.id]).create()

    ForeignKeyConstraint(
        columns=[comment_hashtags.c.comment_id],
        refcolumns=[comments.c.id]).create()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # hashtags = Table('hashtags', meta, autoload=True)
    comment_hashtags = Table('comment_hashtags', meta, autoload=True)
    hashtags = Table('hashtags', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[comment_hashtags.c.user_id],
        refcolumns=[hashtags.c.id]).drop()

    ForeignKeyConstraint(
        columns=[comment_hashtags.c.comment_id],
        refcolumns=[comments.c.id]).drop()
    pass
