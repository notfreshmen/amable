from expects import *

from spec.factories.community_factory import CommunityFactory

from amable.models.community import Community, update_date_modified
from amable import session, db

s = session()

with context('amable.models'):
    with after.all:
        s.query(Community).delete()
        s.commit()

    with context('community'):
        with context('Community'):
            with context('__init__'):
                with it('create'):
                    community = Community(
                        name='The Love',
                        description='for all the love',
                        banner_url='love.png',
                        thumbnail_url='love.png',
                        nsfw=False,
                        active=True
                    )

                    expect(community.name).to(equal('The Love'))
                    expect(community.description).to(equal('for all the love'))
                    expect(community.banner_url).to(equal('love.png'))
                    expect(community.thumbnail_url).to(equal('love.png'))
                    expect(community.num_upvotes).to(equal(0))

            with context('__repr__'):
                with it("returns it's name"):
                    community = CommunityFactory.build()

                    expect(community.__repr__()).to(equal("<Community 'The Love'>"))

        with context('update_date_modified'):
            with it('updates the date for the community'):
                community = CommunityFactory.create()

                date_modified = community.date_modified

                update_date_modified(Community, session, community)

                expect(community.date_modified).not_to(equal(date_modified))
