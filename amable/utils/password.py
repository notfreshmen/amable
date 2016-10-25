import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(
        salt.encode() +
        password.encode()).hexdigest() + ':' + salt


# def check_password(hashed_password, user_password):
#     password, salt = hashed_password.split(':')
#     return password == hashlib.sha256(
#         salt.encode() +
#         user_password.encode()).hexdigest()

def check_password(User, user_input_password):
	salt = User.salt
	hashed_password_to_check = hashlib.sha256(salt.encode() + user_input_password.encode())

	return User.password == hashed_password_to_check

