def shortest(lst: list) -> str:
    return sorted(lst, key=lambda x: len(x))[0]


if __name__ == "__name__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
