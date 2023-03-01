import random
import string


def password_generator(size=8, special_chars=True, digits=True):
    """Generate a random password string of the specified size.

    Args:
        size (int, optional): The length of the password. Defaults to 8. (max size: 52)
        special_chars (bool, optional): Whether to include special characters in the password. Defaults to True.
        digits (bool, optional): Whether to include digits in the password. Defaults to True.

    Returns:
        str: A randomly generated password string consisting of uppercase and lowercase letters, digits, and optionally special characters.
    """

    letters = string.ascii_letters
    if special_chars:
        letters += string.punctuation
    if digits:
        letters += string.digits
    return "".join(random.sample(letters, size))
