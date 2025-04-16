from difflib import get_close_matches

with open("wordlist.txt") as f:
    wordlist = [word.rstrip() for word in f]

text = input("Write text: ")

out_text = []
suggestions = {}
for word in text.split():
    if word.lower() not in wordlist:
        suggestions[word] = get_close_matches(word, wordlist)
        word = f"*{word}*"
    out_text.append(word)

print(" ".join(out_text))
if suggestions:
    print("suggestions:")
    for word, suggestion in suggestions.items():
        print(f"{word}: {", ".join(suggestion)}")
