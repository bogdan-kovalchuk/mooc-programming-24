def transpose(matrix: list) -> None:
    ln = len(matrix)
    for i in range(ln):
        for j in range(i, ln):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)
