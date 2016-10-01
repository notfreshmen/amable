from sqlalchemy import event
from amable.models.user import User
from datetime import datetime as dt


@event.listens_for(User, 'before_update')
def receive_before_update(mapper, connection, target):
    target.date_modified = dt.now().isoformat()
