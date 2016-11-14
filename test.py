from amable import session
# from amable.models.post import Post
from amable.models.comment import Comment
from amable.models.post_report import PostReport
# p = session.query(Post).first()
# print(p.get_comment_tree())

# comment = session.query(Comment).filter_by(id=5).first()

# # print(comment)
# print(comment.has_children())

# print("Children List")
# # print([x ])

# haloCount = session.query(Comment).filter_by(user_id=2).filter(Comment.post.has(answered=False)).count()
# print(haloCount)

# parent = session.query(Comment).filter_by(user_id=3).first()
# parent = session.query(Comment).filter_by(user_id=3).filter(Comment.post.has(answered=False)).first()
# print(parent)

j = session.query(PostReport.parent_id).filter_by(parent_id=5).filter(.group_by(PostReport.parent_id).subquery('j')

a = session.query()

# postReport = session.query(PostReport).filter_by(parent_id=5).all()

print(postReport)

