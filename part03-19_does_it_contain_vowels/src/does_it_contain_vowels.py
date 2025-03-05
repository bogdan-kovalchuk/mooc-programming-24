# Does it contain vowels
string = input("Please type in a string: ")

for vowel in ["a", "e", "o"]:
    if vowel in string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
