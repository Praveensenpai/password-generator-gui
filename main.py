from functools import partial
import string
from random import choices, shuffle


def password_generator(size: int = 8) -> str:
    letters = [
        *(
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits
            + string.punctuation
        )
    ]
    password = choices(letters, k=size)
    shuffle(password)
    return "".join(password)


print(password_generator(10))
password_generator_8 = partial(password_generator, size=10)
print(password_generator_8())
