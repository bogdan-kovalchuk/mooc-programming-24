lst = list()
while True:
    if (item := int(input("New item: "))) == 0:
        break
    lst.append(item)
    print(f"The list now: {lst}")
    print(f"The list in order: {sorted(lst)}")
print("Bye!")
