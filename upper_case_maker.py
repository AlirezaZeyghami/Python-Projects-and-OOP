class UpperCaseIs:
    def __init__(self):
        self.user_input = ""

    def get_input(self):
        self.user_input = input("text: ")

    def make_uppercase(self):
        return self.user_input.upper()


user_upper = UpperCaseIs()
user_upper.get_input()
print(user_upper.make_uppercase())
