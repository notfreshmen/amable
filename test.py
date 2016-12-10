from spec.factories.user_factory import UserFactory

from amable.models.follower import Follower
from amable.models.user import User

from amable import session

session.query(User).delete()
session.commit()

print('hey')
u1 = UserFactory(username="gi")
u2 = UserFactory(username="giii")

session.add(u1)
session.add(u2)

session.commit()

follow = Follower(source_user=u1, target_user=u2)

session.add(follow)
session.commit()
