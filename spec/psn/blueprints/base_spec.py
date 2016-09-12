from expects import *

from amable import app

client = app.test_client()

with context('amable'):
    with context('blueprints'):
        with context('base'):
            with context('index'):
                with it('returns hello world'):
                    res = client.get('/')

                    expect(res.data).to(equal(b'Hello world'))
