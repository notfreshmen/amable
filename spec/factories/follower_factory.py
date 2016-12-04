import factory

from amable import session

from amable.models.follower import Follower

from spec.factories.user_factory import UserFactory


class FollowerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Follower
        sqlalchemy_session = session

    source_user = factory.SubFactory(UserFactory)
    target_user = factory.SubFactory(UserFactory)