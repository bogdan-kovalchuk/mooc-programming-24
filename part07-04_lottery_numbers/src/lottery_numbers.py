from random import sample


def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper + 1))
    return sorted(sample(number_pool, amount))
