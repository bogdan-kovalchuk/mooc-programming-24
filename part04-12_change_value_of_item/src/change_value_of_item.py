lst = [1, 2, 3, 4, 5]
while True:
    idx = int(input("Index:"))
    if idx == -1:
        break
    lst[idx] = int(input("New value:"))
    print(lst)
