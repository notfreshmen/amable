from expects import *
from models.user import User
from models import listen
from amable import session




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
                        phone="8888888888",
                        dob="1999-01-08")

                    userModTime = user.date_modified

                    s = session()
                    s.add(user)
                    s.commit()

                    expect(user.username).to(equal('pablo'))

                    # Update a attribute
                    user.name = "Dom"
                    s.commit()

                    expect(user.name).to(equal('Dom'))
                    expect(user.date_modified).not_to(equal(userModTime))

                    s.delete(user)

            with context('__repr__'):
                with it('returns the username'):
                    user = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="8888888888",
                        dob="1999-01-08")

                    expect(user.__repr__()).to(equal("<User 'pablo'>"))
