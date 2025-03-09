# Line
def line(num: int, string: str) -> None:
    char = "*"
    if string:
        char = string[0]
    print(num * char)


if __name__ == "__main__":
    line(5, "x")
