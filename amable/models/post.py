from datetime import datetime as dt

from amable import db

from .base import Base

from .post_report import PostReport
from .post_upvote import PostUpvote
from .comment import Comment

from sqlalchemy import event
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text_brief = db.Column(db.String(142))
    text_long = db.Column(db.Text)
    answered = db.Column(db.Boolean)
    hashtags = db.Column(db.Text)
    image_url = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    reports = relationship(PostReport, backref="post")
    post_upvotes = relationship(PostUpvote, backref="post")
    comments = relationship(Comment, backref="post")

    def __init__(
            self,
            text_brief,
            text_long,
            hashtags,
            image_url,
            user_id,
            community_id,
            answered=False
    ):
        self.text_brief = text_brief
        self.text_long = text_long
        self.answered = answered
        self.hashtags = hashtags
        self.image_url = image_url
        self.user_id = user_id
        self.community_id = community_id

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Post %r>' % self.id


def before_update_listener(mapper, connection, target):
        # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Post, 'before_update', before_update_listener)
