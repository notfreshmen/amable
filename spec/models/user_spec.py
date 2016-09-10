from expects import *

from psn import User


with context('models'):
    with context('user'):
        with context('User'):
            with context('__init__'):
                with it('sets the username'):
                    user = User('pablo', 'pablo@reev.us')

                    expect(user.username).to(equal('pablo'))

                with it('sets the email'):
                    user = User('pablo', 'pablo@reev.us')

                    expect(user.username).to(equal('pablo'))

            with context('__repr__'):
                with it('returns the username'):
                    user = User('pablo', 'pablo@reev.us')

                    expect(user.__repr__()).to(equal("<User 'pablo'>"))
