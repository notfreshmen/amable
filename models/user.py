from amable import *
from amable import util
from datetime import datetime
from sqlalchemy import event
import hashlib
import uuid

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    salt = db.Column(db.String(128))
    name = db.Column(db.String(128))
    role = db.Column(db.String(10))
    bio = db.Column(db.Text)
    website = db.Column(db.String(128))
    location = db.Column(db.String(128))
    phone = db.Column(db.String(10))
    dob = db.Column(db.DateTime)
    profile_image = db.Column(db.String(128))
    date_created = db.Column(db.String(128))
    date_modified = db.Column(db.String(128))

    def __init__(self, username, email, password, name, bio, website, location, phone, dob, profile_image=None, role=None):
        self.username = username
        self.email = email

        hashedPassword = util.hash_password(password) # Hash the password. SHA256
        splitPassword = hashedPassword.split(":") # Split the password and the salt

        self.password = splitPassword[0]
        self.salt = splitPassword[1]

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

        now = datetime.datetime(year, month, day, hour, minute, second)

        self.date_created = now
        self.date_modified = now



    def __repr__(self):
        return '<User %r>' % self.username



    def after_insert_listener(mapper, connection, target):
        # 'target' is the inserted object
        target.date_modified = datetime.datetime(year, month, day, hour, minute, second)

    event.listen(self, 'after_insert', after_insert_listener)