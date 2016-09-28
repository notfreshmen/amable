from os.path import join
from os.path import dirname

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


load_dotenv(join(dirname(__file__), '..', '.env'))

app = Flask(__name__)
app.config.from_envvar('AMABLE_SETTINGS')


from amable.blueprints.base import base

from amable.utils.assets import assets_env

from models import db
from models.user import User


app.register_blueprint(base)
