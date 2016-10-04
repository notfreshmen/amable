from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event
from sqlalchemy.orm import relationship

from .post import Post
from .community_user import CommunityUser


class Community(Base):
    __tablename__ = 'communities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)
    banner_url = db.Column(db.String(128))
    thumbnail_url = db.Column(db.String(128))
    nsfw = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    num_upvotes = db.Column(db.Integer)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    posts = relationship(Post, backref="community")
    users = relationship(CommunityUser, backref="community")

    def __init__(
            self,
            name,
            description,
            banner_url,
            thumbnail_url,
            nsfw,
            active,
            num_upvotes=0
    ):
        self.name = name
        self.description = description
        self.banner_url = banner_url
        self.thumbnail_url = banner_url
        self.nsfw = nsfw
        self.active = active
        self.num_upvotes = num_upvotes

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Community %r>' % self.name


def before_update_listener(mapper, connection, target):
        # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Community, 'before_update', before_update_listener)
