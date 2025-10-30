class Dog:
    quantity = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.quantity += 1
    

class InputClass:
    def __init__(self):
        self.user_input_name = ""
        self.user_input_age = 0

    def take_input(self):
        self.user_input_name = input("name: ")
        self.user_input_age = int(input("age: "))

    def make_instance(self):
        return Dog(self.user_input_name, self.user_input_age)


ins_inp = InputClass()
while True:
    ins_inp.take_input()
    dog = ins_inp.make_instance()
    print(Dog.quantity)
