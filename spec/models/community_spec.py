from expects import *

from amable.models.community import Community, update_date_modified
from amable import session

from spec.factories.community_factory import CommunityFactory

s = session()

with context('amable.models'):
    with before.each:
        self.community = CommunityFactory.create()

    with after.all:
        s.query(Community).delete()
        s.commit()

    with context('community'):
        with context('Community'):
            with context('__init__'):
                with it('create'):
                    c = Community(
                        name='The Love',
                        description='for all the love',
                        banner_url='love.png',
                        thumbnail_url='love.png',
                        nsfw=False,
                        active=True
                    )

                    expect(c.name).to(equal('The Love'))
                    expect(c.description).to(equal('for all the love'))
                    expect(c.banner_url).to(equal('love.png'))
                    expect(c.thumbnail_url).to(equal('love.png'))
                    expect(c.num_upvotes).to(equal(0))

            with context('__repr__'):
                with it("returns it's name"):
                    expect(self.community.__repr__()).to(equal("<Community 'The Love'>"))

        with context('update_date_modified'):
            with it('updates the date for the community'):
                date_modified = self.community.date_modified

                update_date_modified(Community, session, self.community)

                expect(self.community.date_modified).not_to(equal(date_modified))
