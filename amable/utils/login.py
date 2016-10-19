import sys
import os

from flask_login import LoginManager
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../../')


from amable import app, session
from amable.models.user import User

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()
