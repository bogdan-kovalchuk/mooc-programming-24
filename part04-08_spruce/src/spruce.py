def spruce(size: int):
    print("a spruce!")
    for i in range(size):
        spaces = " " * (size - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)
    trunk = " " * (size - 1) + "*"
    print(trunk)


if __name__ == "__main__":
    spruce(5)
