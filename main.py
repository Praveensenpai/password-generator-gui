import random
import string


def password_generator(size=8):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(letters, size))
    return password


print(password_generator(10))
print(password_generator(size=8))
