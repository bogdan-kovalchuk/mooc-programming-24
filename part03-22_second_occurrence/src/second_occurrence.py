# The second occurrence
string = input("Please type in a string:")
substring = input("Please type in a substring:")

index = string.find(substring)
if index != -1:
    index = string.find(substring, index + len(substring))
    if index != -1:
        print(f"The second occurrence of the substring is at index {index}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
