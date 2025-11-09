# the bingo game (function base)

import random

rand_num = random.randint(0, 10)
guess_left = 3


def Check_answer(answer):
    if answer > rand_num:
        return (False, "Choose a lower number!")
    elif answer < rand_num:
        return (False, "Choose a higher number")
    elif answer == rand_num:
        return (True, "Bingo!")


name = input("Please enter your name: ")
while True:
    if guess_left == 0:
        print(f"{name}, you ran out of guess!\nAnsweer was: {rand_num}")
        break
    answer_input = int(input(f"{name}, please enter your guess number: "))
    answer_result = Check_answer(answer_input)
    if answer_result[0] is False:
        print(answer_result[1])
    else:
        print(answer_result[1])
        break
    guess_left -= 1

print("End of the game!")
