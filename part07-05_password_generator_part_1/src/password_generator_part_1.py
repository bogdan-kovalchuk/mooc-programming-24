import string
import random


def generate_password(lenght: int):
    return "".join(random.sample(list(string.ascii_letters[:26]), lenght))
