from datetime import datetime as dt
from random import randrange

from amable import db, session, cache

from amable.utils.password import hash_password

from .base import Base

from .report import Report
from .post import Post
from .post_upvote import PostUpvote
from .community_user import CommunityUser
from .comment import Comment
from .community_upvote import CommunityUpvote

from sqlalchemy import event
from sqlalchemy.orm import relationship

from flask import flash


s = session()


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
    post_upvotes = relationship(PostUpvote, backref="user")
    community_user = relationship(CommunityUser, backref="user")
    comments = relationship(Comment, backref="user")
    community_upvotes = relationship(CommunityUpvote, backref="user")

    def __init__(self,
                 username,
                 email,
                 password,
                 name,
                 bio=None,
                 website=None,
                 location=None,
                 phone=None,
                 dob=None,
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

        if profile_image is None:
            image_num = format(randrange(1, 11), '03')

            self.profile_image = '/static/img/default{0}.jpg'.format(image_num)
        else:
            self.profile_image = profile_image

        # Default Values
        now = dt.now().isoformat()  # Current Time to Insert into Datamodels
        self.date_created = now
        self.date_modified = now

    def __repr__(self):
        return '<User %r>' % self.username

    def __eq__(self, other):
        return self.email == other.email

    def is_admin(self):
        return self.role == 'admin'

    def in_community(self, community):
        return s.query(CommunityUser).filter_by(community_id=community.id, user_id=self.id).count() == 1

    def viewable_by(self, _):
        return True

    def creatable_by(self, _):
        return True

    def updatable_by(self, user):
        return self == user or user.is_admin()

    def destroyable_by(self, user):
        return self == user or user.is_admin()

    def avatar(self):
        if self.profile_image:
            return self.profile_image
        else:
            return url_for('static', filename='img/default-avatar.jpg')

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    # Praying Hands - Count on Comments
    def get_praying_hands(self):
        phCount = cache.get(self.id + "_praying_hands")
        if phCount is None:
            phCount = session.query(Comment).filter_by(
                user_id=self.id).group_by(Comment.post_id).count()
            cache.set(self.id + "_praying_hands", phCount, timeout=10 * 60)
        return phCount

    # Halo - Count on Comments where post is answered (prayed for)
    def get_halo(self):
        haloCount = cache.get(self.id + "_halo")
        if haloCount is None:
            haloCount = session.query(Comment).filter_by(user_id=self.id).group_by(Comment.post_id).filter(Comment.post.has(answered=True)).count()
            cache.set(self.id + "_halo", haloCount, timeout = 10 * 60)
        return haloCount

    # Hammer - Count of posts that user reported where other people also reported
    def get_hammer(self):
        hammerCount = cache.get(self.id + "_hammer")
        if hammerCount is None:
            hammerCount = session.query()
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def vote_for_community(self, community):
        # First we want to make sure that this user
        # hasn't yet voted for this community
        upvoteCount = s.query(CommunityUpvote).filter_by(
            user_id=self.id,
            community_id=community.id).count()
        if upvoteCount == 0:  # Has not voted
            newUpvote = CommunityUpvote(self, community)
            s.add(newUpvote)
            s.commit()
        else:
            flash("You have already voted for this community")


def update_date_modified(mapper, connection, target):
    # 'target' is the inserted object
    target.date_modified = dt.now().isoformat()


event.listen(User, 'before_update', update_date_modified)
