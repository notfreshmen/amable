from datetime import datetime as dt

from amable import db

from .base import Base

from sqlalchemy import event


class PostUpvote(Base):
    __tablename__ = 'post_upvotes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(self, post, user):
        self.post = post
        self.user = user

        # Default Values
        now = dt.now().isoformat()
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<PostUpvote %r/%r>' % (self.post.id, self.user.username)


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(PostUpvote, 'before_update', update_date_modified)
