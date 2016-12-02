from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


# class PostReport(Base):
class Follower(Base):
    __tablename__ = 'followers'
    source_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    target_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            source_user,
            target_user
    ):
        self.source = source_user
        self.target = target_user

        self.source_id = source_user.id
        self.target_id = target_user.id

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Follower ~ Source : %i | Target : %i>' % (self.source_id, self.target_id)


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Follower, 'before_update', update_date_modified)
