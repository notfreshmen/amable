from expects import *

from amable import session
from amable.models.community_user import CommunityUser, update_date_modified
from amable.models.community import Community
from amable.models.user import User

from spec.factories.community_user_factory import CommunityUserFactory
from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.community_user = CommunityUserFactory()
        session.add(self.community_user)
        session.commit()

    with after.all:
        session.query(CommunityUser).delete()
        session.query(Community).delete()
        session.query(User).delete()
        session.commit()

    with context('community_user'):
        with context('CommunityUser'):
            with context('__init__'):
                with it("create"):
                    community = CommunityFactory.create()
                    user = UserFactory.create()

                    community_user = CommunityUser(
                        community=community,
                        user=user)

                    expect(community_user.user_id).to(equal(user.id))
                    expect(community_user.community_id).to(equal(community.id))
                    expect(community_user.moderator).to(equal(False))

            with context('__repr__'):
                with it('returns the name of the community and the username of the user'):
                    expect(self.community_user.__repr__()).to(contain("<CommunityUser 'The Love'/'pablo"))

        with context('update_date_modified'):
            with it('updates the date modified'):
                date_modified = self.community_user.date_modified

                update_date_modified(CommunityUser, session, self.community_user)

                expect(self.community_user.date_modified).not_to(equal(date_modified))
