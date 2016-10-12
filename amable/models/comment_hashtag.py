from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


class CommentHashtag(Base):
    __tablename__ = 'comment_hashtags'
    comment_id = db.Column(db.Integer,
                           db.ForeignKey('comments.id'),
                           primary_key=True)

    hashtag_id = db.Column(db.Integer,
                           db.ForeignKey('hashtags.id'),
                           primary_key=True)

    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            comment_id,
            hashtag_id
    ):

        self.comment_id = comment_id
        self.hashtag_id = hashtag_id

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<CommentHashtag (Comment : %i | Hashtag %i)>' % (self.comment_id, self.hashtag_id)


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(PostHashtag, 'before_update', update_date_modified)
