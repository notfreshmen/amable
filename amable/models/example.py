from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


# class PostReport(Base):
class XXXX(Base):
    __tablename__ = 'XXXX'
    id = db.Column(db.Integer, primary_key=True)
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            XXXX
    ):

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<XXXX %r>' % self.XXXX


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(XXXX, 'before_update', update_date_modified)
