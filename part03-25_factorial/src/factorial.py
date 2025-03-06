# Factorial
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        n = number
        factorial = 1
        while number >= 1:
            factorial *= number
            number -= 1
        print(f"The factorial of the number {n} is {factorial}")
