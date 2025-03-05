# A framed word
string = input("Word:")
str_len = len(string)
print(30 * "*")
if str_len % 2 == 0:
    spaces = int(((30 - str_len) - 2) / 2)
    print("*" + (spaces * " ") + string + (spaces * " ") + "*")
else:
    spaces = int(((30 - str_len) - 2) / 2)
    print("*" + (spaces * " ") + string + ((spaces + 1) * " ") + "*")
print(30 * "*")
