from expects import *

from amable import session
from amable.models.community_upvote import CommunityUpvote, update_date_modified
from amable.models.community import Community
from amable.models.user import User

from spec.factories.community_upvote_factory import CommunityUpvoteFactory
from spec.factories.post_factory import PostFactory
from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory
from spec.factories.community_user_factory import CommunityUserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.community_upvote = CommunityUpvoteFactory()
        # self.community_upvote = PostFactory()
        s.add(self.community_upvote)
        s.commit()

    with after.all:
        s.rollback()
        s.query(CommunityUpvote).delete()
        s.query(Community).delete()
        s.query(User).delete()
        s.commit()

    with context('community_upvote'):
        with context('CommunityUpvote'):
            with context('__init__'):
                with it('create'):
                    community = CommunityFactory.create()
                    user = UserFactory.create()

                    community_upvote = CommunityUpvote(user, community)

                    expect(community_upvote.community_id).to(
                        equal(community.id))
                    expect(community_upvote.user_id).to(equal(user.id))

            with context('__repr__()'):
                with it('returns the id of the post'):
                    expect(self.community_upvote.__repr__()).to(
                        contain("<User"))

            with context('viewable_by'):
                with context('random user'):
                    with it('returns true'):
                        expect(self.community_upvote.viewable_by(None)).to(be_true)

            with context('creatable_by'):
                with context('not already voted'):
                    with it('returns true'):
                        expect(self.community_upvote.creatable_by(UserFactory())).to(be_true)

                with context('already voted'):
                    with _it('returns false'):
                        expect(self.community_upvote.creatable_by(community_upvote.user)).to(be_false)

            with context('updatable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.community_upvote.updatable_by(None)).to(be_false)

            with context('destroyable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.community_upvote.updatable_by(None)).to(be_false)

        with context('update_date_modified'):
            with it('updates the date for the community upvote'):
                date_modified = self.community_upvote.date_modified

                update_date_modified(
                    CommunityUpvote, session, self.community_upvote)

                expect(self.community_upvote.date_modified).not_to(
                    equal(date_modified))
