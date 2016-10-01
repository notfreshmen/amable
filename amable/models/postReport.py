from amable import db
from datetime import datetime as dt
from sqlalchemy import event

from models import Base


class PostReport(Base):
    __tablename__ = 'post_reports'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    content = db.Column(db.Text)
    reason = db.Column(db.String(64))
    resolved = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(self,
                 user_id,
                 post_id,
                 content,
                 reason="misc"
                 ):

        self.user_id = user_id
        self.post_id = post_id
        self.content = content

        # Available Reasons
        # misc|offensive|mean
        self.reason = reason

        now = dt.now().isoformat

        # Default Values
        self.resolved = False
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<PostReport User : %i | Post : %i>' % self.user_id, self.post_id


def after_insert_listener(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()

event.listen(PostReport, 'after_update', after_insert_listener)
