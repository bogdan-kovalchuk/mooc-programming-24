word_list = []
while (word := input("Word:")) not in word_list:
    word_list.append(word)
print(f"You typed in {len(word_list)} different words")
