def line(num: int, string: str) -> None:
    char = "*"
    if string:
        char = string[0]
    print(num * char)


def triangle(size):
    for i in range(1, size + 1):
        line(i, "#")


if __name__ == "__main__":
    triangle(5)
