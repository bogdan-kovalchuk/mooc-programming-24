num = int(input("Please type in a positive integer:"))
numbers = list(range(-1 * num, 0)) + list(range(1, num + 1))
for n in numbers:
    print(n)