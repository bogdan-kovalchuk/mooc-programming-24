# A word squared
def squared(string: str, num: int) -> None:
    for i in range(num):
        row = ""
        for j in range(num):
            row += string[(i * num + j) % len(string)]
        print(row)


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
