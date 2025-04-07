while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_input = int(input("Function: "))
    if user_input == 1:
        in_finnish = input("The word in Finnish: ")
        in_english = input("The word in English: ")
        with open("dictionary.txt", "a") as f:
            f.write(f"{in_finnish};{in_english}\n")
        print("Dictionary entry added")
    elif user_input == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt") as f:
            d = [entry.rstrip().split(";") for entry in f]
            [
                print(f"{fin} - {en}")
                for fin, en in d
                if search_term in fin or search_term in en
            ]
    elif user_input == 3:
        print("Bye!")
        break
