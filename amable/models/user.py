from datetime import datetime as dt

from amable import db

from amable.utils.password import hash_password

from .base import Base

from .report import Report
from .post import Post
from .post_report import PostReport
from .post_upvote import PostUpvote
from .community_user import CommunityUser
from .comment import Comment

from sqlalchemy import event
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128))
    role = db.Column(db.String(10))
    bio = db.Column(db.Text)
    website = db.Column(db.String(128))
    location = db.Column(db.String(128))
    phone = db.Column(db.String(10))
    dob = db.Column(db.DateTime)
    profile_image = db.Column(db.String(128))
    date_created = db.Column(db.String(128), nullable=False)
    date_modified = db.Column(db.String(128), nullable=False)
    reports = relationship(Report, backref="user")
    posts = relationship(Post, backref="user")
    post_reports = relationship(PostReport, backref="user")
    post_upvotes = relationship(PostUpvote, backref="user")
    community_user = relationship(CommunityUser, backref="user")
    comments = relationship(Comment, backref="user")

    def __init__(self,
                 username,
                 email,
                 password,
                 name,
                 bio,
                 website,
                 location,
                 phone,
                 dob,
                 profile_image=None,
                 role=None
                 ):

        self.username = username
        self.email = email

        # Hash the password. SHA256
        hashedPassword = hash_password(password)

        # Split the password and the salt
        splitPassword = hashedPassword.split(":")

        self.password = splitPassword[0]  # Password
        self.salt = splitPassword[1]     # Salt

        self.name = name

        if role is not None:
            self.role = role
        else:
            self.role = "user"

        self.bio = bio
        self.website = website
        self.location = location
        self.phone = phone
        self.dob = dob

        if profile_image is not None:
            self.profile_image = profile_image
        else:
            self.profile_image = ""

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<User %r>' % self.username


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()


event.listen(User, 'before_update', update_date_modified)
