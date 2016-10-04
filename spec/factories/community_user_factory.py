import factory

from amable import session

from amable.models.community_user import CommunityUser

from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory


class CommunityUserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = CommunityUser
        sqlalchemy_session = session

    community = factory.SubFactory(CommunityFactory)
    user = factory.SubFactory(UserFactory)
