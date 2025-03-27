def times_ten(start_index: int, end_index: int):
    return {i: 10 * i for i in range(start_index, end_index + 1)}


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
