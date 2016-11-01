from spec.factories.comment_factory import CommentFactory
from amable import session

s = session()

topComment = CommentFactory()

subComment1 = CommentFactory(post=topComment.post, parent=topComment)
subComment2 = CommentFactory(post=topComment.post, parent=topComment)
subComment3 = CommentFactory(post=topComment.post, parent=topComment)

subsubComment1 = CommentFactory(post=topComment.post, parent=subComment3)


s.commit()
