def list_of_stars(lst: list)->None:
    for num in lst:
        print(num * '*')


if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])