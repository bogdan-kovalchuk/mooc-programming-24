def count_matching_elements(m: list, element: int) -> int:
    out = 0
    for i in m:
        for j in i:
            if j == element:
                out += 1
    return out


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
