def balanced_brackets(my_string: str) -> bool:
    b = [ch for ch in my_string if ch in "()[]"]
    if not b:
        return True

    if len(b) % 2 == 1:
        return False

    pairs = {")": "(", "]": "["}
    opens, closes = set("(["), set(")]")

    def rec(arr):
        if not arr:
            return True

        if arr[0] in closes or arr[-1] in opens:
            return False

        if pairs.get(arr[-1]) != arr[0]:
            return False

        return rec(arr[1:-1])

    return rec(b)


if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)

    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)
