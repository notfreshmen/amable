from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


class Report(Base):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(128))
    resolved = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'report'
    }

    def __init__(self,
                 title,
                 content,
                 user,
                 category="misc"
                 ):

        self.title = title
        self.content = content
        self.user = user

        # Available Categories
        # misc|bug|question|important
        self.category = category

        # Current Time to Insert into Dataamable.models
        now = dt.now().isoformat

        # Default Values
        self.resolved = False
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Report %r>' % self.title


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()


event.listen(Report, 'before_update', update_date_modified)
