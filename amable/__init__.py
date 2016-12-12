# OS Functions
from os import environ
from os.path import join
from os.path import dirname

from dotenv import load_dotenv

# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Session|Engine(SQLAlchemy)
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

# CSRF
from flask_wtf.csrf import CsrfProtect

# File Uploads
dire = dirname(__file__)
UPLOAD_FOLDER = dire + '/uploads'
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
login_manager.login_view = "/login"


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
