from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


# class PostReport(Base):
class CommunityUpvote(Base):
    __tablename__ = 'community_upvotes'
    community_id = db.Column(db.Integer,
                             db.ForeignKey('communities.id'),
                             primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        primary_key=True)

    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            user,
            community
    ):
        self.user = user
        self.community = community

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Community : %i | Post : %i>' % \
            (self.user_id, self.community_id)


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(CommunityUpvote, 'before_update', update_date_modified)
