# Underlining
while True:
    string = input("Please type in a string:")
    str_len = len(string)
    if str_len == 0:
        break
    print(string)
    print(str_len * "-")
