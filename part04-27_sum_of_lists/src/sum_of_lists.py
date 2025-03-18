def list_sum(a: list, b: list) -> list:
    return [i + j for i, j in zip(a, b)]


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 10, 12]
