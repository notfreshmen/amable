from datetime import datetime as dt

from amable import db

from .base import Base

from .post_report import PostReport
from .post_upvote import PostUpvote
from .post_hashtag import PostHashtag
from .comment import Comment

from sqlalchemy import event
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text_brief = db.Column(db.String(142))
    text_long = db.Column(db.Text)
    answered = db.Column(db.Boolean)
    image_url = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    reports = relationship(PostReport, backref="parent")
    post_upvotes = relationship(PostUpvote, backref="post")
    comments = relationship(Comment, backref="post")
    hashtags = relationship(PostHashtag, backref="post")

    def __init__(
            self,
            text_brief,
            text_long,
            image_url,
            user,
            community,
            answered=False
    ):
        self.text_brief = text_brief
        self.text_long = text_long
        self.answered = answered
        self.image_url = image_url
        self.user = user
        self.community = community

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Post %r>' % self.id

    def viewable_by(self, user):
        return True

    def creatable_by(self, user):
        return user.in_community(self) or user.is_admin()

    def updatable_by(self, user):
        return self.user == user or user in self.community.moderators() or user.is_admin()

    def destroyable_by(self, user):
        return self.user == user or user in self.community.moderators() or user.is_admin()


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Post, 'before_update', update_date_modified)
