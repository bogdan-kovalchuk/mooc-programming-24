def double_items(numbers: list) -> list:
    return list(map(lambda x: 2 * x, numbers))


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
