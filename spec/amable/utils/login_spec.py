from expects import *



from amable import session
from amable.models.user import User, update_date_modified

from amable.utils.login import load_user

from spec.factories.user_factory import UserFactory

s = session()

with context('load_user'):
	with it("loads user"):
		user = UserFactory.create()
		s.commit()
		
		expect(load_user(user.id)).to(equal(user))
		