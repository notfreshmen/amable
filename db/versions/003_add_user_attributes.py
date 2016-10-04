from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    password = Column("password", String(128), nullable=False)
    salt = Column("salt", String(128), nullable=False)
    name = Column("name", String(128))
    role = Column("role", String(10))
    bio = Column("bio", Text)
    website = Column("website", String(128))
    location = Column("location", String(128))
    phone = Column("phone", String(10))
    dob = Column("dob", DateTime)
    profile_image = Column("profile_image", String(128))
    date_created = Column("date_created", DateTime, nullable=False)
    date_modified = Column("date_modified", DateTime, nullable=False)

    password.create(users)
    salt.create(users)
    name.create(users)
    role.create(users)
    bio.create(users)
    website.create(users)
    location.create(users)
    phone.create(users)
    dob.create(users)
    profile_image.create(users)
    date_created.create(users)
    date_modified.create(users)
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    users.c.password.drop()
    users.c.salt.drop()
    users.c.name.drop()
    users.c.role.drop()
    users.c.bio.drop()
    users.c.website.drop()
    users.c.location.drop()
    users.c.phone.drop()
    users.c.dob.drop()
    users.c.profile_image.drop()
    users.c.date_created.drop()
    users.c.date_modified.drop()
    pass
