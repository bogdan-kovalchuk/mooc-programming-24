def find_words(search_term: str):
    with open("words.txt") as f:
        words = [line.strip() for line in f]

    def matches(word):
        if search_term == word:
            return True
        if search_term.startswith("*") and word.endswith(search_term[1:]):
            return True
        if search_term.endswith("*") and word.startswith(search_term[:-1]):
            return True
        if "." in search_term and len(search_term) == len(word):
            return all(sc == wc or sc == "." for sc, wc in zip(search_term, word))
        return False

    return [word for word in words if matches(word)]
