import math

from sqlalchemy import func, desc

from sqlalchemy.sql.expression import label
from sqlalchemy.sql.functions import coalesce

from amable import session

from amable.models.post import Post
from amable.models.post_upvote import PostUpvote

s = session()


class FeedService:
    def __init__(self, user):
        self.user = user

    def communities(self, page=0, per_page=25):
        query = s.query(Post)

        query = query.filter(Post.community_id.in_(self.user.community_ids)) \
                     .order_by(Post.date_created) \
                     .offset(page * per_page) \
                     .limit(per_page)

        return list(query)

    def top(self, page=0, per_page=25):
        upvote_counts = s.query(PostUpvote.post_id, func.count(PostUpvote.id).label('count')) \
                         .group_by(PostUpvote.id) \
                         .subquery()

        total_upvotes = coalesce(upvote_counts.c.count, 0)

        query = s.query(Post, label('total_upvotes', total_upvotes))
        query = query.outerjoin(upvote_counts, upvote_counts.c.post_id == Post.id) \
                     .order_by(desc('total_upvotes')) \
                     .offset(page * per_page) \
                     .limit(per_page)

        return [result[0] for result in list(query)]
