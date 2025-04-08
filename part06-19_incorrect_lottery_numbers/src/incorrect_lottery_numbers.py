def filter_incorrect():
    with open("lottery_numbers.csv") as f_in, open("correct_numbers.csv", "w") as f_out:
        for line in f_in:
            try:
                week_part, numbers_part = line.split(";")
                nums = list(map(float, numbers_part.split(",")))
                if not (
                    any(not num.is_integer() for num in nums)
                    or int(week_part.split()[1]) > 51
                    or len(nums) != 7
                    or max(nums) > 39
                    or min(nums) < 1
                ):
                    f_out.write(line)
            except Exception as e:
                continue
