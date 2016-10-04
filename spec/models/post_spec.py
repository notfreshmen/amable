from expects import *

from amable import session
from amable.models.post import Post, update_date_modified
from amable.models.community import Community
from amable.models.user import User

from spec.factories.post_factory import PostFactory
from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.post = PostFactory.create()

    with after.all:
        s.query(Post).delete()
        s.query(Community).delete()
        s.query(User).delete()
        s.commit()

    with context('post'):
        with context('Post'):
            with context('__init__'):
                with it('create'):
                    community = CommunityFactory.create()
                    user = UserFactory.create()

                    post = Post(
                        text_brief='A short story',
                        text_long='A long story',
                        hashtags='#hashtag',
                        image_url='image.jpg',
                        community=community,
                        user=user
                    )

                    expect(post.community_id).to(equal(community.id))
                    expect(post.user_id).to(equal(user.id))

            with context('__repr__()'):
                with it('returns the id of the post'):
                    expect(self.post.__repr__()).to(contain("<Post"))

        with context('update_date_modified'):
            with it('updates the date for the post'):
                date_modified = self.post.date_modified

                update_date_modified(Post, session, self.post)

                expect(self.post.date_modified).not_to(equal(date_modified))
