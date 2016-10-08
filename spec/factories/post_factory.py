import factory

from amable import session

from amable.models.post import Post

from spec.factories.community_factory import CommunityFactory
from spec.factories.user_factory import UserFactory


class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = session

    text_brief = 'A short story'
    text_long = 'A long story'
    image_url = 'foo.jpg'
    user = factory.SubFactory(UserFactory)
    community = factory.SubFactory(CommunityFactory)
