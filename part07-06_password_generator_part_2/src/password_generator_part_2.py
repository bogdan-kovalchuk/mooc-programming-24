import string
import random


def generate_strong_password(length: int, is_digits: bool, is_punctuation: bool):
    digits = random.randint(1, length - 2) if is_digits else 0
    spec_chars = random.randint(1, length - digits - 1) if is_punctuation else 0
    letters = length - digits - spec_chars

    letter_part = random.choices(string.ascii_lowercase, k=letters)
    digit_part = random.choices(string.digits, k=digits)
    special_part = random.choices("!?=+-()#", k=spec_chars)

    all_chars = letter_part + digit_part + special_part
    random.shuffle(all_chars)

    return "".join(all_chars)
