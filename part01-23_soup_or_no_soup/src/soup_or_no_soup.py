# Write your solution here
name = input("Please tell me your name:")
if name != "Jerry":
    portions = int(input("How many portions of soup?"))
    single_portion_price = 5.90
    print(f"The total cost is {portions*single_portion_price}")
print("Next please!")