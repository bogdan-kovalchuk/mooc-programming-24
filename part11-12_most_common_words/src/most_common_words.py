import string


def most_common_words(filename: str, lower_limit: int) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    text_no_punct = text.translate(str.maketrans("", "", string.punctuation))

    words = text_no_punct.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return {word: count for word, count in word_counts.items() if count >= lower_limit}
