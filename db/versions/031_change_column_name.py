from sqlalchemy import *
from migrate import *

parent_id = Column("parent_id", Integer, nullable=True)
parent = Column("parent", Integer, nullable=True)


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)

    # users.c.password.drop()
    comments.c.parent.drop()

    parent_id.create(comments)
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    comments = Table('comments', meta, autoload=True)

    # users.c.password.drop()
    comments.c.parent_id.drop()

    parent.create(comments)
    pass
