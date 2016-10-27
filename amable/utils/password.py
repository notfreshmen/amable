import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(
        salt.encode() +
        password.encode()).hexdigest() + ':' + salt


# Check Password
# Takes in the User object and the password that the user inputed
def check_password(User, user_input_password):
    salt = User.salt

    hashed_password_to_check = hashlib.sha256(
        salt.encode() + user_input_password.encode()).hexdigest()

    # print("check_password() ~ User.salt : " + str(salt))
    # print("check_password() ~ hashed_password_to_check : " + str(hashed_password_to_check))

    return User.password == hashed_password_to_check
