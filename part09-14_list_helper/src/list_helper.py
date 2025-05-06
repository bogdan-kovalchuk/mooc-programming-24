class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def get_frequency(cls, my_list: list):
        frequency = {}
        for num in my_list:
            frequency[num] = frequency.get(num, 0) + 1
        return frequency

    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequency = ListHelper.get_frequency(my_list)
        return max(frequency.items(), key=lambda x: x[1])[0]

    @classmethod
    def doubles(cls, my_list: list):
        frequency = ListHelper.get_frequency(my_list)
        return len([v for v in frequency.values() if v >= 2])


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
