def load_matrix():
    file_name = "matrix.txt"
    with open(file_name) as f:
        return [list(map(int, line.rstrip().split(","))) for line in f]


def matrix_sum():
    return sum([sum(row) for row in load_matrix()])


def matrix_max():
    return max([max(row) for row in load_matrix()])


def row_sums():
    return [sum(row) for row in load_matrix()]


if __name__ == "__main__":
    print(load_matrix())
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
