print("Person 1:")
name_p1 = input("Name:") 
age_p1 = int(input("Age:"))
print("Person 2:")
name_p2 = input("Name:")
age_p2 = int(input("Age:"))

if age_p1 == age_p2:
    print(f"{name_p1} and {name_p2} are the same age")
elif age_p1 > age_p2:
    print(f"The elder is {name_p1}")
else:
    print(f"The elder is {name_p2}")