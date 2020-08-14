

class Human:
    def __init__(self, height):
        self.height = height


    def change_height(self, height):
        self.height = height


class Person(Human):
    def __init__(self):
        self.height = 164


tom = Person()

print(tom.height)
