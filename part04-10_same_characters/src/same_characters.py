def same_chars(string: str, num1: int, num2: int) -> None:
    if num1 >= len(string) or num2 >= len(string):
        return False
    else:
        return string[num1] == string[num2]


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
