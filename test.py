from amable import session
# from amable.models.post import Post
from amable.models.comment import Comment
# p = session.query(Post).first()
# print(p.get_comment_tree())

comment = session.query(Comment).filter_by(id=5).first()

# print(comment)
print(comment.has_children())

print ("Children List") 
# print([x ])