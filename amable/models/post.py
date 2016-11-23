from datetime import datetime as dt
from collections import OrderedDict

from amable import db, session, cache

from .base import Base

from .post_report import PostReport
from .post_upvote import PostUpvote
from .post_hashtag import PostHashtag
from .comment import Comment

from sqlalchemy import event
from sqlalchemy.orm import relationship

#from CommonMark import commonmark


s = session()


class Post(Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text_brief = db.Column(db.String(142))
    text_long = db.Column(db.Text)
    answered = db.Column(db.Boolean)
    image_url = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    reports = relationship(PostReport, backref="parent")
    post_upvotes = relationship(PostUpvote, backref="post")
    comments = relationship(Comment, backref="post")
    hashtags = relationship(PostHashtag, backref="post")

    def __init__(
            self,
            text_brief,
            text_long,
            image_url,
            user,
            community,
            answered=False
    ):
        self.text_brief = text_brief
        self.text_long = text_long
        self.answered = answered
        self.image_url = image_url
        self.user = user
        self.community = community

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

        # Each post starts with 1 upvote (whomever created the post)
        # We have to insert a record into the post_upvote table
        p_upvote = PostUpvote(self, self.user)
        session.add(p_upvote)
        session.commit()

    def __repr__(self):
        return '<Post %r>' % self.id

    def viewable_by(self, user):
        return True

    def creatable_by(self, user):
        return user.in_community(self) or user.is_admin()

    def updatable_by(self, user):
        return self.user == user or \
            user in self.community.moderators() or \
            user.is_admin()

    def destroyable_by(self, user):
        return self.user == user or \
            user in self.community.moderators() or \
            user.is_admin()

    #def text_brief_markdown(self):
    #    return commonmark(self.text_brief)

    @property
    def comment_tree(self):
        root_tree = OrderedDict()

        root_level = s.query(Comment).filter_by(
            post_id=self.id, parent=None).all()

        def get_children(comment, child_tree):
            for child in comment.children:
                child_tree[child] = get_children(child, OrderedDict())

            return child_tree

        for comment in root_level:
            root_tree[comment] = get_children(comment, OrderedDict())

        return root_tree

    @property
    def total_upvotes(self):
        cacheTotal = cache.get(str(self.id) + "_post_upvotes")

        if cacheTotal is None:
            cacheTotal = session.query(PostUpvote).filter_by(
                post_id=self.id).count()
            cache.set(str(self.id) + "_post_upvotes",
                      cacheTotal, timeout=5 * 60)
        return cacheTotal


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Post, 'before_update', update_date_modified)
