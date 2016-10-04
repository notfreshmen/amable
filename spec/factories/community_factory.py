import factory

from amable import session

from amable.models.community import Community


class CommunityFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Community
        sqlalchemy_session = session

    name = 'The Love'
    description = 'for all the love'
    banner_url = 'love.png'
    thumbnail_url = 'love.png'
    nsfw = False
    active = True
