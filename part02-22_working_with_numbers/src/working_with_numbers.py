n_numbers = 0
numbers_sum = 0
positive_numbers = 0
negative_numbers = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number:"))
    if number == 0:
        break
    n_numbers += 1
    numbers_sum += number
    if number > 0:
        positive_numbers += 1
    else:
        negative_numbers += 1


print(f"Numbers typed in {n_numbers}")
print(f"The sum of the numbers is {numbers_sum}")
print(f"The mean of the numbers is {numbers_sum/n_numbers}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")
