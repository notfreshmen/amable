from expects import *

from amable import session
from amable.models.post_report import PostReport, update_date_modified
from amable.models.user import User
from amable.models.community import Community
from amable.models.post import Post
from amable.models.report import Report
from amable.models.post_upvote import PostUpvote


from spec.factories.post_report_factory import PostReportFactory
from spec.factories.user_factory import UserFactory
from spec.factories.post_factory import PostFactory


s = session()

with context('amable.models'):
    with before.each:
        self.post_report = PostReportFactory()
        session.add(self.post_report)
        session.commit()

    with after.all:
        session.rollback()
        session.query(PostReport).delete()
        session.query(PostUpvote).delete()
        session.query(Report).delete()
        session.query(Post).delete()
        session.query(Community).delete()
        session.query(User).delete()
        session.commit()

    with context('post_report'):
        with context('PostReport'):
            with context('__init__'):
                with _it('create'):
                    user = UserFactory.create()
                    post = PostFactory.create()

                    post_report = PostReport(
                        title="Hey Pablo",
                        content="Jokes!",
                        user=user,
                        post=post
                    )

                    expect(post_report.title).to(equal('Hey Pablo'))
                    expect(post_report.user_id).to(equal(user.id))
                    expect(post_report.parent_id).to(equal(post.id))
                    expect(post_report.post).to(equal(post))

            with context('__repr__()'):
                with it('returns the title of the post_report'):
                    expect(self.post_report.__repr__()).to(
                        equal("<PostReport 'Hey Pablo'>"))

        with context('update_date_modified'):
            with it('updates the date for the post_report'):
                date_modified = self.post_report.date_modified

                update_date_modified(PostReport, session, self.post_report)

                expect(self.post_report.date_modified).not_to(
                    equal(date_modified))
