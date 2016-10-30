from expects import *

from amable import session
from amable.models.post import Post, update_date_modified
from amable.models.community import Community
from amable.models.user import User

from spec.factories.post_factory import PostFactory
from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory
from spec.factories.community_user_factory import CommunityUserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.admin = UserFactory(role='admin')
        self.post = PostFactory()

    with after.all:
        s.rollback()

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
                        expect(self.post.creatable_by(UserFactory())).to(be_false)

                with context('community member'):
                    with _it('returns true'):
                        community_user = CommunityUserFactory(community=self.post.community)

                        expect(self.post.creatable_by(community_user.user)).to(be_true)

            with context('updatable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.post.updatable_by(UserFactory())).to(be_false)

                with context('author'):
                    with it('returns true'):
                        expect(self.post.updatable_by(self.post.user)).to(be_true)

                with context('moderator'):
                    with _it('returns true'):
                        pass

                with context('admin'):
                    with it('returns true'):
                        expect(self.post.updatable_by(self.admin)).to(be_true)

            with context('destroyable_by'):
                with context('random user'):
                    with it('returns false'):
                        expect(self.post.updatable_by(UserFactory())).to(be_false)

                with context('author'):
                    with it('returns true'):
                        expect(self.post.updatable_by(self.post.user)).to(be_true)

                with context('moderator'):
                    with _it('returns true'):
                        pass

                with context('admin'):
                    with it('returns true'):
                        expect(self.post.updatable_by(self.admin)).to(be_true)

        with context('update_date_modified'):
            with it('updates the date for the post'):
                date_modified = self.post.date_modified

                update_date_modified(Post, session, self.post)

                expect(self.post.date_modified).not_to(equal(date_modified))
