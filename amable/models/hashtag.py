from datetime import datetime as dt

from amable import db

from .base import Base

from .post_hashtag import PostHashtag

from sqlalchemy import event
from sqlalchemy.orm import relationship


# class PostReport(Base):
class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(128))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    post_hashtag = relationship(PostHashtag, backref="hashtag")

    def __init__(
            self,
            tag
    ):

        self.tag = tag

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Hashtag %r>' % self.tag


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Hashtag, 'before_update', update_date_modified)
