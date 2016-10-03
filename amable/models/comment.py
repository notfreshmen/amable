from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


# class PostReport(Base):
class Comment(Base):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    hashtags = db.Column(db.Text)
    parent = db.Column(db.Integer)
    upvote_count = db.Column(db.String(128))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            content,
            hashtags,
            parent,
            upvote_count=0
    ):

        self.content = content
        self.hashtags = hashtags
        self.parent = parent

        # Default Values
        now = dt.now().isoformat  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Comment %r>' % self.id


def after_insert_listener(mapper, connection, target):
        # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Comment, 'after_update', after_insert_listener)
