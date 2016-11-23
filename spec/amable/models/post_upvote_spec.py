from expects import *

from amable import session
from amable.models.post_upvote import PostUpvote, update_date_modified
from amable.models.post import Post
from amable.models.community import Community
from amable.models.user import User

from spec.factories.post_upvote_factory import PostUpvoteFactory
from spec.factories.post_factory import PostFactory
from spec.factories.user_factory import UserFactory


s = session()

with context('amable.models'):
    with before.each:
        self.post_upvote = PostUpvoteFactory.create()
        s.add(self.post_upvote)
        s.commit()

    with after.all:
        s.rollback()
        s.query(PostUpvote).delete()
        s.query(Post).delete()
        s.query(Community).delete()
        s.query(User).delete()
        s.commit()

    with context('post_upvote'):
        with context('PostUpvote'):
            with context('__init__'):
                with it('create'):
                    post = PostFactory.create()
                    user = UserFactory.create()

                    post_upvote = PostUpvote(
                        post=post,
                        user=user
                    )

                    s.commit()

                    expect(post_upvote.post_id).to(equal(post.id))
                    expect(post_upvote.user_id).to(equal(user.id))

            with context('__repr__()'):
                with it('returns the id of the upvote'):
                    expect(self.post_upvote.__repr__()).to(contain("<PostUpvote"))

        with context('update_date_modified'):
            with it('updates the date for the post'):
                date_modified = self.post_upvote.date_modified

                update_date_modified(PostUpvote, session, self.post_upvote)

                expect(self.post_upvote.date_modified).not_to(equal(date_modified))
