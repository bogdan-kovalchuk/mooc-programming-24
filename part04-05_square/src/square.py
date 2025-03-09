def line(num: int, string: str) -> None:
    char = "*"
    if string:
        char = string[0]
    print(num * char)


def square(size, character):
    for i in range(size):
        line(size, character)


if __name__ == "__main__":
    square(5, "x")
