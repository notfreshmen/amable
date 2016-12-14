# OS Functions
from os import environ
from os.path import join
from os.path import dirname

from dotenv import load_dotenv

# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

# Session|Engine(SQLAlchemy)
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

# CSRF
from flask_wtf.csrf import CsrfProtect

# File Uploads
UPLOAD_FOLDER = dirname(__file__) + '/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Cache
from werkzeug.contrib.cache import MemcachedCache
cache = MemcachedCache(['127.0.0.1:11211'])

# DotEnv Setup
load_dotenv(join(dirname(__file__), '..', '.env'))

# Environment choice
env = environ.get('AMABLE_ENV')

if env is None:
    env = 'development'

# App setup
app = Flask(__name__)
app.config.from_envvar('AMABLE_%s_SETTINGS' % env.upper())
app.secret_key = 'SshHUD33J6UwTygB'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# DB setup
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
session = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)

# CSRF setup
csrf = CsrfProtect(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'


# Blueprints
from amable.blueprints.base import base
from amable.blueprints.sessions import sessions
from amable.blueprints.posts import posts
from amable.blueprints.communities import communities
from amable.blueprints.users import users
from amable.blueprints.comments import comments

app.register_blueprint(base)
app.register_blueprint(sessions)
app.register_blueprint(communities)
app.register_blueprint(posts)
app.register_blueprint(users)
app.register_blueprint(comments)

# Assets
from amable.utils.assets import assets_env

# Filters
from amable.utils.filters import time_since

# Base
from amable.models.base import Base

# Flask Admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
admin = Admin(app, name='amable', template_mode='bootstrap3')


class MyModelView(ModelView):

    def is_accessible(self):
        if current_user is not None:
            return current_user.role == 'admin'
        else:
            return False

# Admin Views
from amable.models.user import User
from amable.models.post import Post
from amable.models.comment import Comment
from amable.models.community import Community
from amable.models.post_report import PostReport
from amable.models.follower import Follower
admin.add_view(MyModelView(User, session))
admin.add_view(MyModelView(Post, session))
admin.add_view(MyModelView(Comment, session))
admin.add_view(MyModelView(Community, session))
admin.add_view(MyModelView(PostReport, session))
admin.add_view(MyModelView(Follower, session))
