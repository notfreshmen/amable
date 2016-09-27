from os.path import join
from os.path import dirname

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_assets import Environment, Bundle
from sass import compile as sass_compile

from amable.blueprints.base import base

load_dotenv(join(dirname(__file__), '..', '.env'))

app = Flask(__name__)
app.config.from_envvar('AMABLE_SETTINGS')


def sass_filter(_in, out, **kw):
    compiled_sass = sass_compile(
        string=_in.read(),
        include_paths=[join(dirname(__file__), 'assets', 'css', 'lib')]
    )

    out.write(compiled_sass)


env = Environment(app)

env.load_path = [
    join(dirname(__file__), 'assets', 'css'),
    join(dirname(__file__), 'assets', 'jsc')
]


env.register(
    'css',
    Bundle(
        'application.scss',
        filters=[sass_filter],
        output='application.css'
    )
)

env.register(
    'jsc',
    Bundle(
        'lib/jquery-3.1.1.min.js',
        'application.js',
        filters=['jsmin'],
        output='application.js'
    )
)


from models import db
from models.user import User


app.register_blueprint(base)
