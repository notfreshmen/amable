from expects import *

from amable import app

client = app.test_client()

with context('amable'):
    with context('blueprints'):
        with context('base'):
            with context('index'):
                with _it('has a dashboard'):
                    pass
