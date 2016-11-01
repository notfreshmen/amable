import factory

from amable import session

from amable.models.comment import Comment

from spec.factories.user_factory import UserFactory
from spec.factories.post_factory import PostFactory


class CommentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Comment
        sqlalchemy_session = session

    content = 'I hope you smell flowers'
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    parent = None
