from expects import *
from amable.models.community import Community
from amable import session

s = session()

with context('amable.models'):
    with context('communities'):
        with context('Community'):

            with context('__init__'):

                with it('create'):
                    community = Community(
                        name="The Love",
                        description="for all the love",
                        banner_url="love.png",
                        thumbnail_url="love.png",
                        nsfw=False,
                        active=True
                    )
                    s.add(community)
                    s.commit()

                    expect(community.name).to(equal('The Love'))
                    expect(community.description).to(equal('for all the love'))
                    expect(community.banner_url).to(equal('love.png'))
                    expect(community.thumbnail_url).to(equal('love.png'))
                    expect(community.num_upvotes).to(equal(0))

                    s.delete(community)
                    s.commit()

                with it('edit'):
                    community = Community(
                        name="The Love",
                        description="for all the love",
                        banner_url="love.png",
                        thumbnail_url="love.png",
                        nsfw=False,
                        active=True
                    )
                    s.add(community)
                    s.commit()

                    expect(community.name).to(equal('The Love'))
                    expect(community.description).to(equal('for all the love'))
                    expect(community.banner_url).to(equal('love.png'))
                    expect(community.thumbnail_url).to(equal('love.png'))
                    expect(community.num_upvotes).to(equal(0))

                    community.name = "The Hate"
                    s.commit()

                    expect(community.name).to(equal('The Hate'))

                    s.delete(community)
                    s.commit()

            with context("listeners"):
                with it('before_update'):
                    community = Community(
                        name="The Love",
                        description="for all the love",
                        banner_url="love.png",
                        thumbnail_url="love.png",
                        nsfw=False,
                        active=True)

                    s.add(community)
                    s.commit()

                    expect(community.name).to(equal('The Love'))

                    dateMod = community.date_modified

                    community.name = "The Hate"

                    s.commit()

                    expect(community.name).to(equal('The Hate'))
                    expect(community.date_modified).not_to(equal(dateMod))

                    s.delete(community)
                    s.commit()
