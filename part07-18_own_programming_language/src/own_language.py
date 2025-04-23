import string


def run(program):
    def resolve(x):
        return int(variables.get(x, x))

    ops = {
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
        "<": lambda a, b: a < b,
        "<=": lambda a, b: a <= b,
        ">": lambda a, b: a > b,
        ">=": lambda a, b: a >= b,
    }

    locations = {line[:-1]: i for i, line in enumerate(program) if ":" in line}
    variables = {letter: 0 for letter in string.ascii_uppercase}
    result = []

    i = 0
    while i < len(program):
        line = program[i]
        parts = line.split()
        cmd = parts[0]

        if cmd == "PRINT":
            result.append(resolve(parts[1]))
        elif cmd == "MOV":
            variables[parts[1]] = resolve(parts[2])
        elif cmd in {"ADD", "SUB", "MUL"}:
            var1, value = parts[1], resolve(parts[2])
            if cmd == "ADD":
                variables[var1] += value
            elif cmd == "SUB":
                variables[var1] -= value
            elif cmd == "MUL":
                variables[var1] *= value
        elif cmd == "IF":
            var1, op, var2, _, label = parts[1:]
            if ops[op](variables[var1], resolve(var2)):
                i = locations[label]
                continue
        elif cmd == "JUMP":
            i = locations[parts[1]]
            continue
        elif cmd == "END":
            break

        i += 1

    return result
