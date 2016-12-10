from spec.factories.comment_factory import CommentFactory
from spec.factories.post_report_factory import PostReportFactory
from spec.factories.post_upvote_factory import PostUpvoteFactory
from spec.factories.user_factory import UserFactory
from spec.factories.community_factory import CommunityFactory
from spec.factories.community_user_factory import CommunityUserFactory
from spec.factories.post_factory import PostFactory
from amable import session

s = session()

# --- USERS --- #

# We will have some users
user0 = UserFactory()
user1 = UserFactory()
user2 = UserFactory()
user3 = UserFactory()

# --- COMMUNITIES --- #
# Let's have 1 community
community0 = CommunityFactory()
community1 = CommunityFactory(active=False)
community2 = CommunityFactory(active=False)

session.commit()

# Add all of our users to the community
cu0 = CommunityUserFactory(user=user0, community=community0)
cu1 = CommunityUserFactory(user=user1, community=community0)
cu2 = CommunityUserFactory(user=user2, community=community0)

session.commit()

# --- POSTS --- #
# user0 makes a post
post0 = PostFactory(user=user0, community=community0)

# user1 makes a post
post1 = PostFactory(user=user1, community=community0)

session.commit()

# --- COMMENTS --- #
# COMMENT RECURSIVENESS #

# user2 replies to both posts
comment0 = CommentFactory(user=user2, post=post0)
comment1 = CommentFactory(user=user2, post=post1)

session.commit()

# user0 replies to comment0
comment3 = CommentFactory(user=user0, post=post0, parent=comment0)

session.commit()

# user2 replies to comment3 made by user0
comment4 = CommentFactory(user=user2, post=post0, parent=comment3)

session.commit()

# user1 replies to comment0
comment5 = CommentFactory(user=user1, post=post0, parent=comment0)

# --- POST REPORTS --- #

# user 2 and 3 reports post 0
pr0 = PostReportFactory(post=post0, user=user2)
pr1 = PostReportFactory(post=post0, user=user3)

session.commit()

# Lets give post1 9 reports (to test)
for x in range(0, 9):
    session.add(PostReportFactory(post=post1))
    session.commit()

# --- POST UPVOTES --- #

# user 1 upvotes post 0
pu0 = PostUpvoteFactory(post=post0, user=user1)

session.commit()

# topComment = CommentFactory()

# session.commit()

# subComment1 = CommentFactory(post=topComment.post, parent=topComment.id)
# subComment2 = CommentFactory(post=topComment.post, parent=topComment.id)
# subComment3 = CommentFactory(post=topComment.post, parent=topComment.id)

# session.commit()

# subsubComment1 = CommentFactory(post=topComment.post, parent=subComment3.id)


# session.commit()

# print("Community ID: " + str(topComment.post.community.id))

# # Lets create some reports
# postReport = PostReportFactory(post=topComment.post, user=topComment.user)

# postReport2 = PostReportFactory(post=topComment.post, user=subComment1.user)

# # Post upvotes
# postUpvote0 = PostUpvoteFactory(post = topComment.post, user = topComment.post.user)
# postUpvote1 = PostUpvoteFactory(post = topComment.post)

# session.commit()
