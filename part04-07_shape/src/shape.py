def line(num: int, string: str) -> None:
    char = "*"
    if string:
        char = string[0]
    print(num * char)


def triangle(size, char):
    for i in range(1, size + 1):
        line(i, char)


def rectangle(height: int, width: int, char: str):
    for i in range(height):
        line(width, char)


def shape(width, triangle_char, rectangle_height, rectangle_char):
    triangle(width, triangle_char)
    rectangle(rectangle_height, width, rectangle_char)


if __name__ == "__main__":
    shape(5, "x", 2, "o")
