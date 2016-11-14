from spec.factories.comment_factory import CommentFactory
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
