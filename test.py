from amable import session
from amable.models.post import Post
p = session.query(Post).first()
print(p.get_comment_tree())

