from abc import ABC, abstractmethod
import random
import string

class PasswordGenerator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass


class WordsPass(PasswordGenerator):
    def generate(self):
        charactors = string.ascii_letters
        password = ''.join(random.choice(charactors) for _ in range(20))
        return password


class NumbersPass(PasswordGenerator):
    def generate(self):
        digits = string.digits
        password = ''.join(random.choice(digits) for _ in range(20))
        return password


class NumWordPass(PasswordGenerator):
    def generate(self):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(20))
        return password

# --- Test ---
if __name__ == "__main__":
    w = WordsPass()
    n = NumbersPass()
    nw = NumWordPass()

    print("Letters only:", w.generate())
    print("Numbers only:", n.generate())
    print("Mixed:", nw.generate())
