def dict_of_numbers():
    ones = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    return {
        num: (
            ones[num]
            if num < 10
            else (
                teens[num - 10]
                if num < 20
                else (
                    tens[num // 10 - 2]
                    if num % 10 == 0
                    else f"{tens[num // 10 - 2]}-{ones[num % 10]}"
                )
            )
        )
        for num in range(100)
    }


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])  # "two"
    print(numbers[11])  # "eleven"
    print(numbers[45])  # "forty-five"
    print(numbers[99])  # "ninety-nine"
    print(numbers[0])  # "zero"
