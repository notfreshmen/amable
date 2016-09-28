from amable import db
from datetime import datetime as dt
from sqlalchemy import event


class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer)
    category = db.Column(db.String(128))
    resolved = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(self,
                 title,
                 content,
                 user_id,
                 category="misc"
                 ):

        self.title = title
        self.content = content
        self.user_id = user_id

        # Available Categories
        # misc|bug|question|important
        self.category = category

        # Current Time to Insert into Database
        now = dt.now().isoformat

        # Default Values
        self.resolved = False

        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<Report %r>' % self.title


def after_insert_listener(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()

event.listen(Report, 'after_update', after_insert_listener)
