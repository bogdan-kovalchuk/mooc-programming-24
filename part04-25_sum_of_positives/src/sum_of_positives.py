def sum_of_positives(my_list: list) -> int:
    summ = 0
    for num in my_list:
        if num > 0:
            summ += num
    return summ