def no_vowels(string: str) -> str:
    return "".join([x for x in list(string) if x not in ["a", "e", "i", "o", "u"]])


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

    my_string = "aeoli"
    print(no_vowels(my_string))
