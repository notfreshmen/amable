from amable import *


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

    def __init__(self, username, email, password, name, role=None, bio, website, location, phone, dob, profile_image=None):
        self.username = username
        self.email = email

        randString = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))






    def __repr__(self):
        return '<User %r>' % self.username
