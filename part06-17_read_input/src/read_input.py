def read_input(phrase, lower_input, upper_input):
    while True:
        try:
            number = int(input(phrase))
            if number < lower_input or number > upper_input:
                raise ValueError
            print(f"You typed in: {number}")
            return number
        except ValueError:
            print(
                f"You must type in an integer between {lower_input} and {upper_input}"
            )
