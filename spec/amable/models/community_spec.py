from expects import *

from amable.models.community import Community, update_date_modified
from amable import session

from spec.factories.community_factory import CommunityFactory
from spec.factories.community_user_factory import CommunityUserFactory
from spec.factories.user_factory import UserFactory

s = session()

with context('amable.models'):
    with before.each:
        self.community = CommunityFactory()
        s.add(self.community)
        s.commit()

    with after.all:
        s.rollback()
        s.query(Community).delete()
        s.commit()

    with context('community'):
        with context('Community'):
            with context('__init__'):
                with it('creates a community'):
                    c = Community(
                        name='The Love',
                        description='for all the love',
                        banner_url='love.png',
                        thumbnail_url='love.png',
                        nsfw=False,
                    )

                    expect(c.name).to(equal('The Love'))
                    expect(c.description).to(equal('for all the love'))
                    expect(c.banner_url).to(equal('love.png'))
                    expect(c.thumbnail_url).to(equal('love.png'))

                with context('permalink'):
                    with context('passed'):
                        with it('sets it'):
                            c = Community(
                                name='The Love',
                                description='for all the love',
                                banner_url='love.png',
                                thumbnail_url='love.png',
                                nsfw=False,
                                permalink='foobar'
                            )

                            expect(c.permalink).to(equal('foobar'))

                    with context('not passed'):
                        with it('sluggifies it'):
                            c = Community(
                                name='Blah blah',
                                description='for all the love',
                                banner_url='love.png',
                                thumbnail_url='love.png',
                                nsfw=False,
                            )

                            expect(c.permalink).to(equal('blah-blah'))

                        with it('sluggifies it and adds a number if not unique'):
                            c = Community(
                                name='The Love',
                                description='for all the love',
                                banner_url='love.png',
                                thumbnail_url='love.png',
                                nsfw=False,
                            )

                            expect(c.permalink).to(contain('the-love-'))

            with context('__repr__'):
                with it("returns it's name"):
                    expect(self.community.__repr__()).to(equal("<Community 'The Love'>"))

            with context('moderators'):
                with _it("returns the moderators"):
                    # moderator = CommunityUserFactory(moderator=True)
                    #
                    # expect(list(moderator.community.moderators())).to(contain(moderator.user))

                    pass

            with context('viewable_by'):
                with context('any user'):
                    with it('returns true every time'):
                        expect(self.community.viewable_by(None)).to(be_true)

            with context('creatable_by'):
                with context('any user'):
                    with it('returns true every time'):
                        expect(self.community.creatable_by(None)).to(be_true)

            with context('updatable_by'):
                with context('random user'):
                    with it('returns false'):
                        user = UserFactory()

                        expect(self.community.updatable_by(user)).to(be_false)

                with context('moderator'):
                    with _it('returns true'):
                        moderator = CommunityUserFactory(moderator=True)

                        expect(moderator.community.updatable_by(moderator.user)).to(be_true)

                with context('admin'):
                    with it('returns true'):
                        admin = UserFactory(role='admin')

                        expect(self.community.updatable_by(admin)).to(be_true)

            with context('destroyable_by'):
                with context('random user'):
                    with it('returns false'):
                        user = UserFactory()

                        expect(self.community.destroyable_by(user)).to(be_false)

                with context('moderator'):
                    with _it('returns false'):
                        moderator = CommunityUserFactory(moderator=True)

                        expect(moderator.community.destroyable_by(moderator.user)).to(be_true)

                with context('admin'):
                    with it('returns true'):
                        admin = UserFactory(role='admin')

                        expect(self.community.destroyable_by(admin)).to(be_true)

        with context('update_date_modified'):
            with it('updates the date for the community'):
                date_modified = self.community.date_modified

                update_date_modified(Community, session, self.community)

                expect(self.community.date_modified).not_to(equal(date_modified))
