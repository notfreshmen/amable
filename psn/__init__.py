from flask import Flask

from psn.blueprints.base import base


app = Flask(__name__)

app.register_blueprint(base)
