from amable import session
from amable.models.post_upvote import PostUpvote
from amable.models.post import Post
from amable.models.comment import Comment
from amable.models.user import User
from amable.models.post_report import PostReport

# a = session.query(Post).filter_by(user_id = 19).all()
# upvoteCount = 0
# for b in a:
#     upvoteCount += b.total_upvotes

# print(upvoteCount)

u = session.query(User).filter_by(id=19).first()
print(u.get_knee())