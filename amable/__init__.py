# OS Functions
from os import environ
from os.path import join
from os.path import dirname

from dotenv import load_dotenv

# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Session|Engine(SQLAlchemy)
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


# DotEnv Setup
load_dotenv(join(dirname(__file__), '..', '.env'))

# Environment choice
env = environ.get('AMABLE_ENV')

if env is None:
    env = 'development'

# App Setup
app = Flask(__name__)
app.config.from_envvar('AMABLE_%s_SETTINGS' % env.upper())

# DB Setup
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
session = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)

# Blueprints
from amable.blueprints.base import base as base_blueprint
from amable.blueprints.users import users as users_blueprint

app.register_blueprint(base_blueprint)
app.register_blueprint(users_blueprint)

# Assets
from amable.utils.assets import assets_env

# Filters
from amable.utils.filters import time_since

# Base
from amable.models.base import Base
