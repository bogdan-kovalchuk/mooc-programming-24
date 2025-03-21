def longest_series_of_neighbours(lst: list) -> int:
    max_length = 1
    current_length = 1

    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


if __name__ == "__main__":
    my_list = [1, 2]
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3]
    print(longest_series_of_neighbours(my_list))
