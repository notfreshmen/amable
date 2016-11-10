import factory

from amable import session

from amable.models.community_upvote import CommunityUpvote

from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory


class CommentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = CommunityUpvote
        sqlalchemy_session = session

    user = factory.SubFactory(UserFactory)
    community = factory.SubFactory(CommunityFactory)
