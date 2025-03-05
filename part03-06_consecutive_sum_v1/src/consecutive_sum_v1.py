# The sum of consecutive numbers, version 1
limit = int(input("Limit:"))

sum_of_numbers = 0
number = 1
while sum_of_numbers < limit:
    sum_of_numbers += number
    number += 1
print(sum_of_numbers)
