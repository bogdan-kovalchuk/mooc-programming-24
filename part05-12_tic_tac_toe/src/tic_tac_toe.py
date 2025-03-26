def play_turn(game_board: list, x: int, y: int, piece: str):
    if 2 >= x >= 0 and 2 >= y >= 0 and not game_board[y][x]:
        game_board[y][x] = piece
        return True
    return False


if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)

    game_board = [["", "O", ""], ["O", "", ""], ["", "", "O"]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)
