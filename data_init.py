from spec.factories.comment_factory import CommentFactory
from spec.factories.post_report_factory import PostReportFactory
from spec.factories.post_upvote_factory import PostUpvoteFactory
from spec.factories.user_factory import UserFactory
from amable import session

s = session()

# We will have 3 Users
user0 = UserFactory()
user1 = UserFactory()
user2 = UserFactory()


s.commit()






# topComment = CommentFactory()

# s.commit()

# subComment1 = CommentFactory(post=topComment.post, parent=topComment.id)
# subComment2 = CommentFactory(post=topComment.post, parent=topComment.id)
# subComment3 = CommentFactory(post=topComment.post, parent=topComment.id)

# s.commit()

# subsubComment1 = CommentFactory(post=topComment.post, parent=subComment3.id)


# s.commit()

# print("Community ID: " + str(topComment.post.community.id))

# # Lets create some reports
# postReport = PostReportFactory(post=topComment.post, user=topComment.user)

# postReport2 = PostReportFactory(post=topComment.post, user=subComment1.user)

# # Post upvotes
# postUpvote0 = PostUpvoteFactory(post = topComment.post, user = topComment.post.user)
# postUpvote1 = PostUpvoteFactory(post = topComment.post)

# s.commit()
