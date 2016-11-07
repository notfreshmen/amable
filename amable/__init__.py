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


# DotEnv Setup
load_dotenv(join(dirname(__file__), '..', '.env'))

# Environment choice
env = environ.get('AMABLE_ENV')

if env is None:
    env = 'development'

# App setup
app = Flask(__name__)
app.config.from_envvar('AMABLE_%s_SETTINGS' % env.upper())
app.secret_key = 'domislove'

# DB setup
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
session = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)

# CSRF setup
csrf = CsrfProtect(app)

# Blueprints
from amable.blueprints.base import base as base_blueprint
from amable.blueprints.users import users as users_blueprint

app.register_blueprint(base_blueprint)
app.register_blueprint(users_blueprint)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Blueprints
from amable.blueprints.base import base
from amable.blueprints.sessions import sessions
from amable.blueprints.posts import posts 

app.register_blueprint(base)
app.register_blueprint(sessions)
app.register_blueprint(posts)

# Assets
from amable.utils.assets import assets_env

# Filters
from amable.utils.filters import time_since

# Base
from amable.models.base import Base
