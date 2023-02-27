import random
import string


def password_generator(size=8, special_chars=True, digits=True):
    letters = string.ascii_letters
    if special_chars:
        letters += string.punctuation
    if digits:
        letters += string.digits
    return "".join(random.sample(letters, size))
