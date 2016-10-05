import factory

from amable import session

from amable.models.user import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = session

    username = factory.Sequence(lambda n: 'pablo%d' % n)
    email = factory.Sequence(lambda n: 'pablo%d@pablo.com' % n)
    password = 'pablo'
    name = 'Pablo'
    bio = 'Pablo'
    website = 'reev.us'
    location = 'pablo'
    phone = '4018888888'
    dob = '1999-01-08'
