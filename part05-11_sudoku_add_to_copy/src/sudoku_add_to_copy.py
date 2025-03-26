def print_sudoku(sudoku: list) -> None:
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print(" ", end="")
        print()
        if (i + 1) % 3 == 0:
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    new_sudoku = [x[:] for x in sudoku]
    new_sudoku[row_no][column_no] = number
    return new_sudoku


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
