def most_common_character(string: str) -> str:
    d = {}
    for ch in string:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return max(d, key=d.get)


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
