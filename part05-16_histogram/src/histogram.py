def histogram(string: str):
    d = {}
    for letter in string:
        if letter not in d:
            d[letter] = 0
        d[letter] += 1

    for letter, count in d.items():
        print(letter, "*" * count)


if __name__ == "__main__":
    histogram("statistically")
