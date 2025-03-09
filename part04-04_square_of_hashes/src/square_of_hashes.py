# A square of hashes
def line(num: int, string: str) -> None:
    char = "*"
    if string:
        char = string[0]
    print(num * char)


def square_of_hashes(size):
    for i in range(size):
        line(size, "#")


if __name__ == "__main__":
    square_of_hashes(5)
