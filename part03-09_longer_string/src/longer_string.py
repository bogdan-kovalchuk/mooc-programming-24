# The longer string
str1 = input("Please type in string 1:")
str2 = input("Please type in string 2:")

len_str1 = len(str1)
len_str2 = len(str2)

if len_str1 > len_str2:
    print(f"{str1} is longer")
elif len_str1 < len_str2:
    print(f"{str2} is longer")
else:
    print("The strings are equally long")
