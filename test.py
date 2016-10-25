from amable.utils.password import check_password
from spec.factories.user_factory import UserFactory

u = UserFactory()

print ("User password : " + u.password)
print ("User salt: " + u.salt)

print(check_password(u,"pablo"))