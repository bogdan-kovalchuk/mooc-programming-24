num1 = int(input("Please type in the first number"))
num2 = int(input("Please type in another number:"))

if num1 == num2:
    print(f"The numbers are equal!")
else:
    print(f"The greater number was: {max(num1, num2)}")