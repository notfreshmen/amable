import sys
import os

from flask_assets import Environment, Bundle
from sass import compile as sass_compile


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../../')


from amable import app


# Helper so we don't have to write out the assets path over and over
def assets_path(*paths):
    return os.path.join(os.path.dirname(__file__), '..', 'static', *paths)


# Create a new assets environment attached to our app
assets_env = Environment(app)

# Tell assets where our assets are located
assets_env.load_path = [
    assets_path('css'),
    assets_path('jsc')
]

# Register the CSS assets
assets_env.register(
    'css',
    Bundle(
        'application.css',
        filters=[],
        output='application.css'
    )
)

# Resgister the JS assets
assets_env.register(
    'jsc',
    Bundle(
        'application.js',
        filters=[],
        output='application.js'
    )
)
