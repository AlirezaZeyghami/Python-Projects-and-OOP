# the bingo game (oop base)

import random


class BingoGame:
    player_list = []

    def __init__(self):
        self.name = input("Please enter your name: ")
        self.__rand_num = random.randint(0, 10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)

    def Check_answer(self):
        answer = int(input(f"\n{self.name}, please enter your guess: "))
        if answer > self.__rand_num:
            print("Choose a lower number!")
        elif answer < self.__rand_num:
            print("Choose a higher number")
        elif answer == self.__rand_num:
            print("Bingo!")
            self.__win_state = True
        self.__minus_guess_left()
        print(f"{self.__guess_left} guess(es) left!")

    def __minus_guess_left(self):
        self.__guess_left -= 1

    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        return False
    
    def has_won(self):
        return self.__win_state
    
    @classmethod
    def has_game_winner(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False


class GameController:
    def __init__(self):
        while True:
            for player in BingoGame.player_list:
                if not player.has_won():
                    player.Check_answer()
            if BingoGame.has_game_winner():
                break


if __name__ == "__main__":
    while True:
        order = input("What do you want to do?\nOrder: ")
        if order == "add":
            BingoGame()
        elif order == "start":
            GameController()
        elif order == "exit":
            break
