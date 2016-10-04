from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    reports = Table('reports', meta, autoload=True)
    post_reports = Table('post_reports', meta, autoload=True)
    users = Table('users', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[post_reports.c.user_id],
        refcolumns=[users.c.id]).drop()

    post_reports.drop()


def downgrade(migrate_engine):
    post_reports = Table(
        'post_reports', meta,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer),
        Column('post_id', Integer),
        Column('content', Text),
        Column('reason', String(64)),
        Column('resolved', Boolean),
        Column('date_created', DateTime, unique=False),
        Column('date_modified', DateTime, unique=False)
    )

    users = Table('users', meta, autoload=True)

    ForeignKeyConstraint(
        columns=[post_reports.c.user_id],
        refcolumns=[users.c.id]).create()

    post_reports.create()
