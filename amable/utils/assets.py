import sys
import os

from flask_assets import Environment, Bundle
from sass import compile as sass_compile


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../../')


from amable import app


# Helper so we don't have to write out the assets path over and over
def assets_path(*paths):
    return os.path.join(os.path.dirname(__file__), '..', 'assets', *paths)


# Helper so we don't have to write our node_modules path over and over
def node_modules_path(*paths):
    return os.path.join(os.path.dirname(__file__), '..', '..', 'node_modules', *paths)


# A assets filter for compiling SCSS/Sass. We can't use the command-line tool
# because it's can't find files references in `@import` directives
def sass_filter(_in, out, **kw):
    compiled_sass = sass_compile(
        string=_in.read(),
        include_paths=[assets_path('css', 'lib')]
    )

    out.write(compiled_sass)


# Create a new assets environment attached to our app
assets_env = Environment(app)

# Tell assets where our assets are located
assets_env.load_path = [
    assets_path('css'),
    assets_path('jsc'),
    node_modules_path()
]

# Register the CSS assets
assets_env.register(
    'css',
    Bundle(
        'application.scss',
        filters=[sass_filter],
        output='application.css'
    )
)

# Resgister the JS assets
assets_env.register(
    'jsc',
    Bundle(
        'jquery/dist/jquery.js',
        'application.js',
        filters=['jsmin'],
        output='application.js'
    )
)
