from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    communities = Table('communities', meta, autoload=True)

    # users.c.password.drop()
    communities.c.num_upvotes.drop()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    communities = Table('communities', meta, autoload=True)

    # password = Column("password", String(128), nullable=False)
    num_upvotes = Column("num_upvotes", Integer, nullable=False, unique=False)

    # password.create(users)
    communities.create(num_upvotes)
    pass
