import factory

from amable import session

from amable.models.community import Community


class CommunityFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Community
        sqlalchemy_session = session

    name = 'The Love'
    description = 'for all the love'
    banner_url = 'http://dsedutech.org/images/demo/placement_banner1.jpg'
    thumbnail_url = 'http://i.imgur.com/7mo7QHW.gif'
    nsfw = False
