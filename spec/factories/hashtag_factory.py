import factory

from amable import session

from amable.models.hashtag import Hashtag


class HashtagFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Hashtag
        sqlalchemy_session = session

    tag = 'reevus'
