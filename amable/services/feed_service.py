import math

from amable import session

from amable.models.post import Post

s = session()

class FeedService:
    def __init__(self, user, page=0, per_page=25, filters=dict(communities=[])):
        self.user = user
        self.page = page
        self.per_page = per_page
        self.filters = filters

    def filtered(self):
        query = s.query(Post).filter(Post.community_id.in_(self.user.community_ids))

        if self.filters.get('communities') != []:
            query = query.filter(Post.community_id.in_(self.filters.get('communities')))

        return query

    def current_posts(self):
        query = self.filtered()

        offset = self.page * self.per_page

        query = query.order_by(Post.date_created)

        query = query.offset(offset)

        query = query.limit(self.per_page)

        return query

    def pages_remaining(self):
        total = self.filtered().count()

        total_pages = math.ceil(total / self.per_page)

        return total_pages - (self.page + 1)
