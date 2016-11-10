from datetime import datetime as dt

from amable import db, session

from slugify import slugify

from .base import Base

from sqlalchemy import event, func
from sqlalchemy.orm import relationship

from .post import Post
from .community_user import CommunityUser
from .community_upvote import CommunityUpvote
from .user import User


s = session()


class Community(Base):
    __tablename__ = 'communities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)
    permalink = db.Column(db.String(128))
    banner_url = db.Column(db.String(128))
    thumbnail_url = db.Column(db.String(128))
    nsfw = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    num_upvotes = db.Column(db.Integer)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    posts = relationship(Post, backref="community")
    users = relationship(CommunityUser, backref="community")
    upvotes = relationship(CommunityUpvote, backref="community")

    def __init__(
            self,
            name,
            description,
            banner_url,
            thumbnail_url,
            nsfw,
            active,
            permalink=None,
            num_upvotes=0
    ):
        self.name = name
        self.description = description
        self.banner_url = banner_url
        self.thumbnail_url = thumbnail_url
        self.nsfw = nsfw
        self.active = active
        self.num_upvotes = num_upvotes

        if permalink:
            self.permalink = permalink
        else:
            candidate = slugify(self.name)

            count = s.query(Community).filter(Community.permalink.like(candidate)).count()

            if count == 0:
                self.permalink = candidate
            else:
                self.permalink = candidate + "-" + str(count)

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'banner_url': self.banner_url,
            'thumbnail_url': self.thumbnail_url,
            'nsfw': self.nsfw,
            'active': self.active,
            'num_upvotes': self.num_upvotes,
            'date_created': self.date_created,
        }

    def __repr__(self):
        return '<Community %r>' % self.name

    def moderators(self):
        community_users = s.query(CommunityUser.user_id).filter_by(community_id=self.id, moderator=True).subquery('community_mods')

        return s.query(User).filter(User.id == community_users.c.user_id)

    def viewable_by(self, _):
        return True

    def creatable_by(self, _):
        return True

    def updatable_by(self, user):
        return user in list(self.moderators()) or user.is_admin()

    def destroyable_by(self, user):
        return user.is_admin()


def update_date_modified(mapper, connection, target):
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Community, 'before_update', update_date_modified)
