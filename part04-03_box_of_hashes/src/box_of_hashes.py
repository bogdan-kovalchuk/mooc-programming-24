# A box of hashes
def line(num: int, string: str) -> None:
    char = "*"
    if string:
        char = string[0]
    print(num * char)


def box_of_hashes(height):
    for i in range(height):
        line(10, "#")


if __name__ == "__main__":
    box_of_hashes(5)
