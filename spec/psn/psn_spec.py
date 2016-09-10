from expects import *

from psn import *
from flask import Flask


with context('psn'):
    with context('app'):
        with it('is a Flask instance'):
            expect(app).to(be_a(Flask))

        with it('registers a base Blueprint'):
            expect(app.blueprints).to(have_key('base'))
