lst = []
while True:
    print(f"The list is now {lst}")
    user_input = input("a(d)d, (r)emove or e(x)it: ").lower()

    if user_input == "d":
        lst.append(lst[-1] + 1 if lst else 1)
    elif user_input == "r" and lst:
        lst.pop()
    elif user_input == "x":
        break

print("Bye!")
