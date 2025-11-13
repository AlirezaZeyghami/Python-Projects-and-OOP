# the hangman game (functional)


def get_first_gamer_word():
    return input("1st gamer, please enter your word: ").strip().lower()


def get_second_gamer_guess():
    return input("2nd gamer, please enter your guess: ").strip().lower()


def check_guess(hidden_word, true_guess, guess):
    if guess in hidden_word:
        true_guess.add(guess)
        print("True guess!")
        return True
    else:
        print("Wrong guess!")
        return False


def display_word(hidden_word, true_guesses):
    display_word = ''.join([letter if letter in true_guesses else '_' for letter in hidden_word])
    print("Word: ", display_word)
    return display_word


def hangman():
    hidden_word = get_first_gamer_word()
    true_guesses = set()
    wrong_guesses = 0
    max_guesses = 6

    while wrong_guesses < max_guesses:
        display_word(hidden_word, true_guesses)
        guess = get_second_gamer_guess()

        if guess in true_guesses:
            continue
        result = check_guess(hidden_word, true_guesses, guess)

        if not result:
            wrong_guesses += 1
            print(f"Remaining chances: {max_guesses - wrong_guesses}")

        if all(letter in true_guesses for letter in hidden_word):
            print(f"You won! hidden word was: {hidden_word}")
            break
    else:
        print(f"Game over! hidden word was: {hidden_word}")


hangman()
