def who_won(game_board: list) -> int:
    player_one_scores = 0
    player_two_scores = 0
    for row in game_board:
        for val in row:
            if val == 1:
                player_one_scores += 1
            elif val == 2:
                player_two_scores += 1
    if player_one_scores > player_two_scores:
        return 1
    elif player_one_scores < player_two_scores:
        return 2
    else:
        return 0
