import string

layers = int(input("Layers:"))
letters = list(string.ascii_uppercase)
size = 2 * layers - 1
box = [[0] * size for _ in range(size)]

k = size // 2
for i in range(k + 1):
    for c in range(-i, i + 1):
        box[k + i][k + c] = letters[i]
        box[k - i][k + c] = letters[i]
        box[k + c][k + i] = letters[i]
        box[k + c][k - i] = letters[i]


for row in box:
    for val in row:
        print(val, end="")
    print()
