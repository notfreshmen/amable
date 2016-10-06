from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


# class PostReport(Base):
class PostHashtag(Base):
    __tablename__ = 'post_hashtags'
    post_id = db.Column(db.Integer, primary_key=True)
    hashtag_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            post_id,
            hashtag_id
    ):

        self.post_id = post_id
        self.hashtag_id = hashtag_id

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<PostHashTag (Post : %i | Hashtag %i)>' % (self.post_id, self.hashtag_id)


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(PostHashtag, 'before_update', update_date_modified)
