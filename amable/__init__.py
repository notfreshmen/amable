# OS Functions
from os.path import join
from os.path import dirname

from dotenv import load_dotenv

# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Models

# Blueprints
from amable.blueprints.base import base

# Session|Engine(SQLAlchemy)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# DotEnv Setup
load_dotenv(join(dirname(__file__), '..', '.env'))

# App Setup
app = Flask(__name__)
app.config.from_envvar('AMABLE_SETTINGS')
app.register_blueprint(base)

# DB Setup
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
session = sessionmaker()
session.configure(bind=engine)
db = SQLAlchemy(app)
