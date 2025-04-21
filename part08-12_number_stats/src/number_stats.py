# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum

    def average(self):
        average = 0
        if self.sum:
            average = self.sum / self.numbers
        return average


print("Please type in integer numbers:")
all_nums = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    number = int(input())

    if number == -1:
        break

    all_nums.add_number(number)
    if number % 2 == 0:
        even.add_number(number)
    else:
        odd.add_number(number)

print(f"Sum of numbers: {all_nums.get_sum()}")
print(f"Mean of numbers: {all_nums.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")
