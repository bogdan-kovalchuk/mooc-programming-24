# Write your solution here


weekly_cafeteria_visits = int(input("How many times a week do you eat at the student cafeteria?"))
student_lunch_price = float(input("The price of a typical student lunch?"))
weekly_grocery_expense = float(input("How much money do you spend on groceries in a week?"))

weekly = weekly_cafeteria_visits * student_lunch_price + weekly_grocery_expense
dayli = weekly / 7

print("Average food expenditure:")
print(f"Daily: {dayli} euros")
print(f"Weekly: {weekly} euros")