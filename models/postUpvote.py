from amable import db
from datetime import datetime as dt
from sqlalchemy import event

class PostUpvote(db.Model):
    __tablename__ = 'post_upvotes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

        now = dt.now().isoformat
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<PostUpvote User : %i Post : %i>' % self.user_id, self.post_id


def after_insert_listener(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(PostUpvote, 'after_update', after_insert_listener)
