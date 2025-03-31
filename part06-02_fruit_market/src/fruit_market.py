def read_fruits() -> dict:
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            fruit, weight = line.rstrip().split(";")
            fruits[fruit] = float(weight)
    return fruits


if __name__ == "__main__":
    print(read_fruits())
