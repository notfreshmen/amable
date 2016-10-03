from expects import *
from amable.models.community_user import CommunityUser
from amable.models.user import User
from amable.models.community import Community
from amable import session

s = session()

with context('amable.models'):
    with context('community_users'):
        with context('CommunityUser'):

            with context('__init__'):

                with it("create"):
                    user = User(
                        username="pablo",
                        email="pablo@pablo.com",
                        password="pablo",
                        name="Pablo",
                        bio="Pablo",
                        website="reev.us",
                        location="pablo",
                        phone="4018888888",
                        dob="1999-01-08")

                    community = Community(
                        name="The Love",
                        description="for all the love",
                        banner_url="love.png",
                        thumbnail_url="love.png",
                        nsfw=False,
                        active=True
                    )

                    s.add(user)
                    s.add(community)
                    s.commit()

                    community_user = CommunityUser(
                        user_id=user.id,
                        community_id=community.id)

                    expect(community_user.user_id).to(equal(user.id))
                    expect(community_user.community_id).to(equal(community.id))
                    expect(community_user.moderator).to(equal(False))

                    s.delete(user)
                    s.delete(community)
                    s.commit()
