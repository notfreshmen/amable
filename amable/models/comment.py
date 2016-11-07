from datetime import datetime as dt

from amable import db, session

from .base import Base
from .comment_hashtag import CommentHashtag

from sqlalchemy import event
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    parent = db.Column(db.Integer, db.ForeignKey('comments.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    upvote_count = db.Column(db.String(128))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    hashtags = relationship(CommentHashtag, backref="post")
    children = relationship("Comment", lazy='joined', join_depth=10)

    def __init__(
            self,
            content,
            user,
            post,
            parent=None,
            upvote_count=0
    ):

        self.content = content
        self.user = user
        self.post = post
        self.parent = parent
        self.upvote_count = 0

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Comment %r>' % self.id

    def has_children(self):
        return session.query(Comment).filter_by(parent=self.id).count() > 0


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Comment, 'before_update', update_date_modified)
