from datetime import datetime as dt

from amable import db

from .base import Base
from .report import Report

from sqlalchemy import event


class PostReport(Report):
    parent_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __init__(self,
                 title,
                 content,
                 user,
                 post,
                 category="misc"
                 ):

        self.parent = post

        super().__init__(
            title=title,
            content=content,
            user=user,
            category=category
        )


    def __repr__(self):
        return '<PostReport %r>' % self.title


    def post(self):
        return self.parent


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(PostReport, 'before_update', update_date_modified)
