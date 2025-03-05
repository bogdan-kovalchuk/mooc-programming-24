# Find the first substring
word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = word.find(char)

if index != -1 and index + 2 < len(word):
    print(word[index : index + 3])
