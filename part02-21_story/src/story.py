story = ""
previous_word = ""
while True:
    word = input("Please type in a word:")
    if word == 'end' or previous_word == word:
        print(story)
        break
    story += word + " "
    previous_word = word
