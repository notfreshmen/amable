from expects import *

from amable import app

client = app.test_client()

with context('amable'):
    with context('blueprints'):
        with context('users'):
            with context('show'):
                with it('returns the user page'):
                    res = client.get('/pablo')

                    expect(res.data).to(contain(b'pablo'))

            with context('new'):
                with _it('returns the join page'):
                    pass


            with context('create'):
                with _it('creates a new user'):
                    pass

                with _it('logs in the new user'):
                    pass

                with _it('redirects to the dashboard'):
                    pass


            with context('edit'):
                with _it('return the account page'):
                    pass


            with context('update'):
                with _it('updates the user'):
                    pass

                with _it('redirects back to the account page'):
                    pass


            with context('destroy'):
                with _it('destroys the user'):
                    pass

                with _it('redirects back to the index'):
                    pass
