def begin_with_vowel(words: list):
    return [w for w in words if w.lower().startswith(("a", "e", "i", "o", "u"))]
