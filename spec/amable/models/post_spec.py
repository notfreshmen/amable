from expects import *

from amable import session
from amable.models.post import Post, update_date_modified
from amable.models.community import Community
from amable.models.user import User
from amable.models.post_upvote import PostUpvote
from amable.models.post_report import PostReport

from spec.factories.post_factory import PostFactory
from spec.factories.post_report_factory import PostReportFactory
from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory
from spec.factories.community_user_factory import CommunityUserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.admin = UserFactory(role='admin')
        self.post = PostFactory()
        session.add(self.admin)
        session.add(self.post)
        session.commit()

    with after.all:
        session.rollback()
        session.query(PostUpvote).delete()
        session.query(PostReport).delete()
        session.query(Post).delete()
        session.query(Community).delete()
        session.query(User).delete()
        session.commit()

    with context('post'):
        with context('Post'):
            with context('__init__'):
                with it('create'):
                    community = CommunityFactory.create()
                    user = UserFactory.create()

                    post = Post(
                        text_brief='A short story',
                        text_long='A long story',
                        image_url='image.jpg',
                        community=community,
                        user=user
                    )

                    expect(post.community_id).to(equal(community.id))
                    expect(post.user_id).to(equal(user.id))

            with context('__repr__()'):
                with it('returns the id of the post'):
                    expect(self.post.__repr__()).to(contain("<Post"))

            with context('viewable_by'):
                with context('random user'):
                    with it('returns true'):
                        expect(self.post.viewable_by(None)).to(be_true)

            with context('creatable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.post.creatable_by(
                            UserFactory())).to(be_false)

                with context('community member'):
                    with _it('returns true'):
                        community_user = CommunityUserFactory(
                            community=self.post.community)

                        expect(self.post.creatable_by(
                            community_user.user)).to(be_true)

            with context('updatable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.post.updatable_by(
                            UserFactory())).to(be_false)

                with context('author'):
                    with it('returns true'):
                        expect(self.post.updatable_by(
                            self.post.user)).to(be_true)

                with context('moderator'):
                    with _it('returns true'):
                        pass

                with context('admin'):
                    with it('returns true'):
                        expect(self.post.updatable_by(self.admin)).to(be_true)

            with context('destroyable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.post.updatable_by(
                            UserFactory())).to(be_false)

                with context('author'):
                    with it('returns true'):
                        expect(self.post.updatable_by(
                            self.post.user)).to(be_true)

                with context('moderator'):
                    with _it('returns true'):
                        pass

                with context('admin'):
                    with it('returns true'):
                        expect(self.post.updatable_by(self.admin)).to(be_true)

            with context('can_be_shown'):
                with it('cache and reports'):
                    # Let's create a post and 5 reports
                    post = PostFactory()
                    session.commit()
                    prArray = []

                    for x in range(0, 5):
                        newPR = PostReportFactory(post=post)
                        session.add(newPR)
                        session.commit()

                    expect(post.can_be_shown()).to(equal(True))

                    # Lets add 5 more
                    for x in range(0, 5):
                        newPR = PostReportFactory(post=post)
                        session.add(newPR)
                        session.commit()

                    # Should still be True until we invalidate
                    expect(post.can_be_shown()).to(equal(True))

                    # Now it will be False
                    expect(post.can_be_shown(True)).to(equal(False))

        with context('update_date_modified'):
            with it('updates the date for the post'):
                date_modified = self.post.date_modified

                update_date_modified(Post, session, self.post)

                expect(self.post.date_modified).not_to(equal(date_modified))
