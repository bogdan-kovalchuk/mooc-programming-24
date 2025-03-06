# First letters of words
sentence = input("Please type in a sentence:")

if len(sentence) > 0:
    print(sentence[0])
    idx = sentence.find(" ")
    while idx != -1:
        print(sentence[idx + 1])
        idx = sentence.find(" ", idx + 1)
