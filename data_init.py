from spec.factories.comment_factory import CommentFactory
from spec.factories.post_report_factory import PostReportFactory
from amable import session

s = session()

topComment = CommentFactory()

s.commit()

subComment1 = CommentFactory(post=topComment.post, parent=topComment.id)
subComment2 = CommentFactory(post=topComment.post, parent=topComment.id)
subComment3 = CommentFactory(post=topComment.post, parent=topComment.id)

s.commit()

subsubComment1 = CommentFactory(post=topComment.post, parent=subComment3.id)


s.commit()

print("Community ID: " + str(topComment.post.community.id))

# Lets create some reports
postReport = PostReportFactory(post=topComment.post, user=topComment.user)

postReport2 = PostReportFactory(post=topComment.post, user=subComment1.user)

s.commit()
