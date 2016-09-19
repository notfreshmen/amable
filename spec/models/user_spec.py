from expects import *

from amable import User


with context('models'):
    with context('user'):
        with context('User'):
            with context('__init__'):
                with it('sets the username'):
                    user = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="4018888888",
                        dob="1999-01-08")

                    expect(user.username).to(equal('pablo'))

                with it('change attribute'):
                    user = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="4018888888",
                        dob="1999-01-08")

                    userModTime = user.date_modified

                    # Update a attribute
                    user.name = "Dom"

                    expect(user.date_modified == userModTime).to.be.false

            with context('__repr__'):
                with it('returns the username'):
                    user = User('pablo', 'pablo@reev.us')

                    expect(user.__repr__()).to(equal("<User 'pablo'>"))
