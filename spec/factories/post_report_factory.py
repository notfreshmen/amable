import factory

from amable import session

from amable.models.post_report import PostReport

from spec.factories.user_factory import UserFactory
from spec.factories.post_factory import PostFactory


class PostReportFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = PostReport
        sqlalchemy_session = session

    title = "Hey Pablo"
    content = "Jokes!"
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
