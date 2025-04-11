import random


def roll(die: str):
    return random.choice({"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}[die])


def play(die1: str, die2: str, times: int):
    out = [0, 0, 0]
    for i in range(times):
        one = roll(die1)
        two = roll(die2)
        if one > two:
            out[0] += 1
        elif one < two:
            out[1] += 1
        else:
            out[2] += 1
    return tuple(out)
