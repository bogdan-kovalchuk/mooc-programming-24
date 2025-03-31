def largest() -> int:
    with open("numbers.txt") as new_file:
        return max((int(line.rstrip()) for line in new_file))
