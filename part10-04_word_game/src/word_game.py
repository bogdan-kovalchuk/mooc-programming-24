# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    vowels = "aeiouAEIOU"

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vovels_pl1 = len([1 for ch in player1_word if ch in MostVowels.vowels])
        vovels_pl2 = len([1 for ch in player2_word if ch in MostVowels.vowels])
        if vovels_pl1 > vovels_pl2:
            return 1
        elif vovels_pl1 < vovels_pl2:
            return 2
        else:
            return 0


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if (
            (player1_word == "scissors" and player2_word == "paper")
            or (player1_word == "paper" and player2_word == "rock")
            or (player1_word == "rock" and player2_word == "scissors")
            or (
                player1_word in ["scissors", "paper", "rock"]
                and player2_word not in ["scissors", "paper", "rock"]
            )
        ):
            return 1
        elif (
            (player2_word == "scissors" and player1_word == "paper")
            or (player2_word == "paper" and player1_word == "rock")
            or (player2_word == "rock" and player1_word == "scissors")
            or (
                player2_word in ["scissors", "paper", "rock"]
                and player1_word not in ["scissors", "paper", "rock"]
            )
        ):
            return 2
        else:
            return 0
