# Flip the pairs
number = int(input("Please type in a number: "))
for i in range(1, number + 1, 2):
    if i + 1 <= number:
        print(i + 1)
    print(i)
