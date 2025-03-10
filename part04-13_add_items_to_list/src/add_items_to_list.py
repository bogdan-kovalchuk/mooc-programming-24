items = int(input("How many items:"))
lst = []
for i in range(1, items + 1):
    item = int(input(f"Item {i}: "))
    lst.append(item)
print(lst)
