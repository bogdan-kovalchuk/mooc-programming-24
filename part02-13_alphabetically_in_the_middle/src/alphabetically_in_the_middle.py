letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")

letter = None
if letter1 > letter2 > letter3 or letter1 < letter2 < letter3:
    letter = letter2
elif letter1 > letter3 > letter2 or letter1 < letter3 < letter2:
    letter = letter3
elif letter2 > letter1 > letter3 or letter2 < letter1 < letter3:
    letter = letter1

print(f"The letter in the middle is {letter}")