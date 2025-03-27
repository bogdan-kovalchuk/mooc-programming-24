def invert(dictionary: dict):
    temp = {v: k for k, v in dictionary.items()}
    dictionary.clear()
    dictionary.update(temp)
