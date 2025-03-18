def palindromes(s: str) -> bool:
    return s == s[::-1]
    
while True:
    s = input("Please type in a palindrome: ")
    is_palindrome = palindromes(s)
    if is_palindrome:
        print(f"{s} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
