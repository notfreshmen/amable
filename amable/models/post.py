from datetime import datetime as dt

from amable import db

from .base import Base

from .post_report import PostReport
from .post_upvote import PostUpvote
from .post_hashtag import PostHashtag
from .comment import Comment

from sqlalchemy import event
from sqlalchemy.orm import relationship

from CommonMark import commonmark


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

    def __repr__(self):
        return '<Post %r>' % self.id

    def viewable_by(self, user):
        return True

    def creatable_by(self, user):
        return user.in_community(self) or user.is_admin()

    def updatable_by(self, user):
        return self.user == user or user in self.community.moderators() or user.is_admin()

    def destroyable_by(self, user):
        return self.user == user or user in self.community.moderators() or user.is_admin()

    def text_brief_markdown(self):
        return commonmark(self.text_brief)

    def get_comment_tree(self):
        # First lets get all the comments for this post
        comments = self.comments
        newComments = []
        parentComments = []
        currComment = None
        currParent = None
        i = 0
        print(comments)
        # Ok so first lets find our parent comments
        # Parent comments will have comments[index].parent = None
        # We will do one pass through all of them
        for idx, comment in enumerate(comments):
            if comment.parent is None:
                parentComments.append(comment)
                comments.remove(comment)

        # Lets assign the first comment we are looking at
        currParent = parentComments.pop()
        currComment = currParent

        newComments.append(currComment)

        while (comments.length > 0):
            # Does the currPost have children?
            if currComment.has_children():
                commentList = [x for x in comments if x.parent=currComment.id]

                for subComment in commentList:
                    newComments.insert(newComments.index(currComment) + 1, subComment)
                    comments.remove(subComment)
            else:



            

            
            


        print(comments)

        return parentComments

        
            



def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()  # Update Date Modified


event.listen(Post, 'before_update', update_date_modified)
