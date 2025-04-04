def filter_solutions():
    with (
        open("solutions.csv") as f_solutions,
        open("correct.csv", "w") as f_correct,
        open("incorrect.csv", "w") as f_incorrect,
    ):
        for line in f_solutions:
            _, expression, result = line.split(";")
            if "+" in expression:
                num1, num2 = map(int, expression.split("+"))
                num = num1 + num2
            elif "-" in expression:
                num1, num2 = map(int, expression.split("-"))
                num = num1 - num2
            elif "/" in expression:
                num1, num2 = map(int, expression.split("/"))
                num = num1 / num2
            elif "*" in expression:
                num1, num2 = map(int, expression.split("*"))
                num = num1 * num2

            target_file = f_correct if num == int(result) else f_incorrect
            target_file.write(line)
