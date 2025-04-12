from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

new_millennium_eve = datetime(2000, 1, 1)

birthday = datetime(year, month, day)

if new_millennium_eve > birthday:
    days = (new_millennium_eve - birthday).days - 1
    print(f"You were {days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
