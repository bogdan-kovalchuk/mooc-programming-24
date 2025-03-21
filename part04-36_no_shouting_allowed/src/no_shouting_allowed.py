def no_shouting(my_list: list) -> list:
    return [x for x in my_list if not x.isupper()]


if __name__ == "__main__":
    my_list = [
        "ABC",
        "def",
        "UPPER",
        "ANOTHERUPPER",
        "lower",
        "another lower",
        "Capitalized",
    ]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
