import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    encrypted = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

    return encrypted + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    encrypted = hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    return password == crypted
