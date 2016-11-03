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
                    s.query(User).delete()
                    s.commit()

                with it('returns the user page'):
                    res = client.get('/{0}'.format(self.user.username))

                    expect(res.data).to(contain(b'pablo'))

            with context('new'):
                with it('returns the join page'):
                    res = client.get('/join')

                    expect(res.data).to(contain(b'Join'))

            with context('create'):
                with it('creates a new user'):
                    user = UserFactory.build()

                    res = client.post('/users', data=dict(
                        username=user.username,
                        name='Foobar',
                        email=user.email,
                        password='foobar',
                        password_confirmation='foobar'
                    ), follow_redirects=True)

                    expect(s.query(User).filter_by(username=user.username).count()).to(equal(1))

                with _it('logs in the new user'):
                    pass

                with it('redirects to the dashboard'):
                    user = UserFactory.build()

                    res = client.post('/users', data=dict(
                        username=user.username,
                        name='Foobar',
                        email=user.email,
                        password='foobar',
                        password_confirmation='foobar'
                    ), follow_redirects=True)

                    print(res.headers['location'])

                    expect(res.location).to(equal('/'))

            with context('edit'):
                with _it('return the account page'):
                    pass

            with context('update'):
                with _it('updates the user'):
                    pass

                with _it('redirects back to the account page'):
                    pass

            with context('destroy'):
                with it('destroys the user'):
                    res = client.delete('/{0}'.format(self.user.id))

                    expect(s.query(User).filter_by(id=self.user.id).count()).to(equal(0))

                with _it('redirects back to the index'):
                    pass
