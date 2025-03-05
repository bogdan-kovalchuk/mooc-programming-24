# The sum of consecutive numbers, version 2
limit = int(input("Limit:"))

sum_of_numbers = 1
number = 2
str_sum_of_numbers = "1"
while sum_of_numbers < limit:
    sum_of_numbers += number
    str_sum_of_numbers += f" + {number}"
    number += 1

print(f"The consecutive sum: {str_sum_of_numbers} = {sum_of_numbers}")
