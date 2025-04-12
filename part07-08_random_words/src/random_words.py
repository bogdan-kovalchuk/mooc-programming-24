import random


def words(n: int, beginning: str):
    with open("words.txt") as f:
        return random.sample([w.rstrip() for w in f if w.startswith(beginning)], n)
