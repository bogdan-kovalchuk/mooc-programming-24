# Find all the substrings
word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = 0

while True:
    index = word.find(char, index)
    if index == -1 or index + 2 >= len(word):
        break
    print(word[index : index + 3])
    index += 1
