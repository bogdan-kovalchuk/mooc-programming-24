# Chessboard
def chessboard(num: int):
    for i in range(num):
        row = "".join("1" if (i + j) % 2 == 0 else "0" for j in range(num))
        print(row)


if __name__ == "__main__":
    chessboard(3)
    chessboard(6)
