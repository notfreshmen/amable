from expects import *

from amable import session

from amable.models.post import Post
from amable.models.community import Community
from amable.models.user import User

from spec.factories.user_factory import UserFactory

from amable.services.feed_service import FeedService


s = session()

with context('amable.services.feed_service'):
    with context('FeedService'):
        with before.each:
            self.user = UserFactory()

            s.add(self.user)
            s.commit()

        with after.each:
            s.rollback()
            s.query(Post).delete()
            s.query(Community).delete()
            s.query(User).delete()
            s.commit()

        with context('__init__'):
            with it('sets the user'):
                service = FeedService(user=self.user)

                expect(service.user).to(equal(self.user))
