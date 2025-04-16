import string


def change_case(orig_string: str):
    letters = list(orig_string)
    for i, letter in enumerate(letters):
        if letter.isupper():
            letters[i] = letter.lower()
        elif letter.islower():
            letters[i] = letter.upper()
    return "".join(letters)


def split_in_half(orig_string: str):
    i = int(len(orig_string) / 2)
    return orig_string[:i], orig_string[i:]


def remove_special_characters(orig_string: str):
    new_string = list()
    for char in orig_string:
        if char.isalnum() or char.isspace():
            new_string.append(char)
    return "".join(new_string)
