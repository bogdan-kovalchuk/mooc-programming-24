def factorials(n: int):
    fact = {1: 1}
    for i in range(2, n + 1):
        fact[i] = i * fact[i - 1]
    return fact


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
