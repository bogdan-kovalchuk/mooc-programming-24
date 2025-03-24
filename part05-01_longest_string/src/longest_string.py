def longest(strings: list) -> str:
    return max(strings, key=lambda x: len(x))


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
