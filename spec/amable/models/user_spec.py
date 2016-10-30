from expects import *

from amable import session
from amable.models.user import User, update_date_modified

from spec.factories.user_factory import UserFactory
from spec.factories.community_user_factory import CommunityUserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.user = UserFactory()
        self.admin = UserFactory(role='admin')

    with after.all:
        s.rollback()

    with context('user'):
        with context('User'):
            with context('__init__'):
                with it('create'):
                    u = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="4018888888",
                        dob="1999-01-08",
                        profile_image='pablo.jpg',
                        role='admin')

                    expect(u.username).to(equal('pablo'))
                    expect(u.profile_image).to(equal('pablo.jpg'))
                    expect(u.role).to(equal('admin'))

            with context('__repr__'):
                with it("returns it's username"):
                    expect(self.user.__repr__()).to(contain("<User 'pablo"))

            with context('is_admin'):
                with context('for admins'):
                    with it('returns true'):
                        expect(self.admin.is_admin()).to(be_true)

                with context('for others'):
                    with it('returns false'):
                        expect(self.user.is_admin()).to(be_false)

            with context('in_community'):
                with context('community member'):
                    with _it('returns true'):
                        community_user = CommunityUserFactory(user=self.user)

                        expect(self.user.in_community(community_user.community)).to(be_true)

            with context('viewable_by'):
                with context('any user'):
                    with it('returns true every time'):
                        expect(self.user.viewable_by(None)).to(be_true)

            with context('creatable_by'):
                with context('any user'):
                    with it('returns true every time'):
                        expect(self.user.creatable_by(None)).to(be_true)

            with context('updatable_by'):
                with context('self'):
                    with it('returns true'):
                        expect(self.user.updatable_by(self.user)).to(be_true)

                with context('other'):
                    with it('returns false'):
                        expect(self.user.updatable_by(UserFactory.build())).to(be_false)

                with context('admin'):
                    with it('returns true'):
                        expect(self.user.updatable_by(self.admin)).to(be_true)

            with context('destroyable_by'):
                with context('self'):
                    with it('returns true'):
                        expect(self.user.destroyable_by(self.user)).to(be_true)

                with context('other'):
                    with it('returns false'):
                        expect(self.user.destroyable_by(UserFactory.build())).to(be_false)

                with context('admin'):
                    with it('returns true'):
                        expect(self.user.destroyable_by(self.admin)).to(be_true)

        with context('update_date_modified'):
            with it('updates the date for the user'):
                date_modified = self.user.date_modified

                update_date_modified(User, session, self.user)

                expect(self.user.date_modified).not_to(equal(date_modified))
