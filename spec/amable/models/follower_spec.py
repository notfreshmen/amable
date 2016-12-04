from expects import *

from amable import session

from amable.models.follower import Follower
from amable.models.user import User
from amable.models.community_user import CommunityUser

from spec.factories.follower_factory import FollowerFactory
from spec.factories.user_factory import UserFactory


with context('amable.models'):
    with before.each:
        self.user1 = UserFactory()
        self.user2 = UserFactory()
        self.follower = FollowerFactory(source_user=self.user1,target_user=self.user2)
        session.add(self.user1)
        session.add(self.user2)
        session.add(self.follower)
        session.commit()

    with after.all:
        session.query(CommunityUser).delete()
        session.query(Follower).delete()
        session.query(User).delete()
        session.commit()

    with context('follower'):
        with context('Follower'):
            with context('__init__'):
                with it("create"):
                    expect(self.follower.source_id).to(equal(self.user1.id))
                    expect(self.follower.target_id).to(equal(self.user2.id))

            with context('__repr__'):
                with it("Return Representation"):
                    expect(self.follower.__repr__()).to(contain("<Follower ! Source :"))
