with open("wordlist.txt") as f:
    wordlist = [word.rstrip() for word in f]

text = input("Write text: ")
out_text = []
for word in text.split():
    if word.lower() not in wordlist:
        word = f"*{word}*"
    out_text.append(word)
print(" ".join(out_text))
