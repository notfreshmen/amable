from models import db
from datetime import datetime as dt
from sqlalchemy import event

class XXXX(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    XXXX = db.Column(db.String(128))
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(
            self,
            XXXX
            ):

        # Default Values
        now = dt.now().isoformat # Current Time to Insert into Database
        self.date_created = now 
        self.date_modified = now

    def __repr__(self):
        return '<XXXX %r>' % self.XXXX

def after_insert_listener(mapper, connection, target):
        # 'target' is the inserted object
    target.date_modified = dt.now().isoformat() # Update Date Modified

event.listen(XXXX, 'after_update', after_insert_listener)

        
