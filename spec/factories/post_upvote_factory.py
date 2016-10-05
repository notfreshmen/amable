import factory

from amable import session

from amable.models.post_upvote import PostUpvote

from spec.factories.post_factory import PostFactory
from spec.factories.user_factory import UserFactory


class PostUpvoteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = PostUpvote
        sqlalchemy_session = session

    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
