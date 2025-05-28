from math import sqrt


def square_roots(lst: list):
    return [sqrt(item) for item in lst]


if __name__ == "__main__":
    lines = square_roots([1, 2, 3, 4])
    for line in lines:
        print(line)
