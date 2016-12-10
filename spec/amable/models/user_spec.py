from expects import *

from amable import session
from amable.utils.password import check_password
from amable.models.user import User, update_date_modified
from amable.models.comment import Comment
from amable.models.post_upvote import PostUpvote
from amable.models.post import Post
from amable.models.community import Community
from amable.models.post_report import PostReport


from spec.factories.user_factory import UserFactory
from spec.factories.community_user_factory import CommunityUserFactory
from spec.factories.comment_factory import CommentFactory
from spec.factories.post_factory import PostFactory
from spec.factories.post_report_factory import PostReportFactory
from spec.factories.post_upvote_factory import PostUpvoteFactory


s = session()

with context('amable.models'):
    with before.each:
        self.user = UserFactory()
        self.admin = UserFactory(role='admin')
        session.add(self.user)
        session.add(self.admin)
        session.commit()

    with after.all:
        session.rollback()
        session.query(PostUpvote).delete()
        session.query(PostReport).delete()
        session.query(Post).delete()
        session.query(Community).delete()
        session.query(User).delete()
        session.commit()

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

                        expect(self.user.in_community(
                            community_user.community)).to(be_true)

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
                        expect(self.user.updatable_by(
                            UserFactory.build())).to(be_false)

                with context('admin'):
                    with it('returns true'):
                        expect(self.user.updatable_by(self.admin)).to(be_true)

            with context('destroyable_by'):
                with context('self'):
                    with it('returns true'):
                        expect(self.user.destroyable_by(self.user)).to(be_true)

                with context('other'):
                    with it('returns false'):
                        expect(self.user.destroyable_by(
                            UserFactory.build())).to(be_false)

                with context('admin'):
                    with it('returns true'):
                        expect(self.user.destroyable_by(
                            self.admin)).to(be_true)

            with context('get_praying_hands'):
                with it('cache and counts'):
                    # Create a couple of comments for the user
                    com0 = CommentFactory(user=self.user)
                    com1 = CommentFactory(user=self.user)
                    com2 = CommentFactory(user=self.user)

                    session.commit()

                    expect(self.user.get_praying_hands()).to(equal(3))

                    # Now we are going to check the cache
                    # Delete a comment and the praying hands should still = 3
                    session.query(Comment).filter_by(id=com0.id).delete()
                    session.commit()

                    expect(self.user.get_praying_hands()).to(equal(3))

                    # Now lets force invalidation and see if it changes
                    expect(self.user.get_praying_hands(True)).to(equal(2))

                    # Cleanup
                    session.query(Comment).delete()
                    session.query(PostUpvote).delete()
                    session.query(Post).delete()
                    session.query(Community).delete()
                    session.commit()

            with context('get_halo'):
                with it('cache and counts'):
                    com0 = CommentFactory(user=self.user)
                    com1 = CommentFactory(user=self.user)

                    com0.post.answered = True

                    session.commit()

                    expect(self.user.get_halo()).to(equal(1))

                    # Lets make the other comment answered too!
                    # We should still get 1 because of cache
                    com1.post.answered = True
                    session.commit()

                    expect(self.user.get_halo()).to(equal(1))

                    # Now lets force invalidation, should get 2
                    expect(self.user.get_halo(True)).to(equal(2))

                    # Cleanup
                    session.query(Comment).delete()
                    session.query(PostUpvote).delete()
                    session.query(Post).delete()
                    session.query(Community).delete()
                    session.commit()

            with context('get_hammer'):
                with it('cache and counts'):
                    # Our user needs to report a post!
                    post0 = PostFactory()

                    postR0 = PostReportFactory(post=post0, user=self.user)

                    # And another user to report the post
                    user0 = UserFactory()

                    postR1 = PostReportFactory(post=post0, user=user0)

                    session.commit()

                    # Now we can expect get_knee to return 1
                    expect(self.user.get_hammer()).to(equal(1))

                    # Test the cache
                    post1 = PostFactory()

                    postR2 = PostReportFactory(post=post1, user=self.user)
                    postR3 = PostReportFactory(post=post1, user=user0)

                    # if NO cache this should now = 2,
                    # but we expect to still = 1
                    expect(self.user.get_hammer()).to(equal(1))

                    # Now lets invalidate the cache and we should expect 2
                    expect(self.user.get_hammer(True)).to(equal(2))

                    # Cleanup
                    session.query(PostReport).delete()
                    session.query(PostUpvote).delete()
                    session.query(Post).delete()
                    session.query(Community).delete()
                    session.commit()

            with context('get_knee'):
                with it('cache and counts'):
                    post0 = PostFactory(user=self.user)

                    user0 = UserFactory()

                    pu0 = PostUpvoteFactory(post=post0, user=user0)

                    session.commit()

                    expect(self.user.get_knee()).to(equal(1))

                    # Lets add another upvote
                    user1 = UserFactory()
                    pu1 = PostUpvoteFactory(post=post0, user=user1)

                    session.commit()

                    # Should stay the same
                    expect(self.user.get_knee()).to(equal(1))

                    # Should change on force of invalidation
                    expect(self.user.get_knee(True)).to(equal(1))

                    # Cleanup
                    session.query(PostUpvote).delete()
                    session.query(Post).delete()
                    session.query(Community).delete()
                    session.commit()

            with context('set_password'):
                with it('changes the password'):
                    self.user.set_password('foobar')

                    expect(check_password(self.user, 'foobar')).to(be_true)

        with context('update_date_modified'):
            with it('updates the date for the user'):
                date_modified = self.user.date_modified

                update_date_modified(User, session, self.user)

                expect(self.user.date_modified).not_to(equal(date_modified))
