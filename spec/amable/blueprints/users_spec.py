from expects import *

from amable import app, session
from amable.models.user import User

from spec.factories.user_factory import UserFactory


client = app.test_client()

s = session()

with context('amable'):
    with context('blueprints'):
        with context('users'):
            with context('show'):
                with before.all:
                    self.user = UserFactory()

                with after.all:
                    s.rollback()

                with it('returns the user page'):
                    res = client.get('/{0}'.format(self.user.username))

                    expect(res.data).to(contain(b'pablo'))

            with context('new'):
                with _it('returns the join page'):
                    res = client.get('/join')

                    expect(res.data).to(contain(b'Join'))

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
