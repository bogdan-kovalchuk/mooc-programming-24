def mean(lst: list) -> float:
    return sum(lst) / len(lst)


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
