# the hangman game (oop)


class Hangman:
    def __init__(self):
        self.owner = input("Match owner, enter hidden word: ").strip().lower()
        self.true_guesses = set()
        self.wrong_guesses = 0
        self.max_guesses = 6

    def display_word(self):
        display = ''.join([letter if letter in self.true_guesses else '_' for letter in self.owner])
        print("Word:", display)
        return display

    def get_guess(self):
        return input("Player, enter your guess: ").strip().lower()

    def check_guess(self, guess):
        if guess in self.owner:
            self.true_guesses.add(guess)
            print("Correct!")
            return True
        else:
            self.wrong_guesses += 1
            print(f"Wrong! Remaining chances: {self.max_guesses - self.wrong_guesses}")
            return False

    def play(self):
        while self.wrong_guesses < self.max_guesses:
            self.display_word()
            guess = self.get_guess()

            if guess in self.true_guesses:
                print("You already guessed that.")
                continue

            self.check_guess(guess)

            if all(letter in self.true_guesses for letter in self.owner):
                print(f"You won! The word was: {self.owner}")
                return

        print(f"Game over! The word was: {self.owner}")


game = Hangman()
game.play()
