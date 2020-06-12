

from random import random, randint
profile_list = []


class Profile:
    def __init__(self, name, bank_id, balance):
        self.name = name
        self.bank_id = bank_id
        self.balance = balance
        self.job = "No job"
        self.salary = "No salary"
        self.loan = False
        self.food = 0

    def get_info(self):
        print("Person name: " + self.name)
        print("Person's bank ID: " + str(self.bank_id))
        print("Persons's available balance: " + str(self.balance))

    def food_consumption(self):
        self.food = self.food - 1

    def pay_loan(self, bank):
        import company
        down_payment = (self.loan / (5*12))
        self.balance = self.balance - down_payment
        bank.balance = bank.balance + down_payment
        print(self.loan/(5*12))


def transactions(user1, user2, amount):
    user1.balance = user1.balance + amount
    user2.balance = user2.balance - amount


def make_person(name):

    def make_id():
        new_id = "ID" + str(randint(1000000000, 9999999999))
        for i in range(len(profile_list)):
            if len(profile_list) > 0:
                while new_id == profile_list[i].name:
                    new_id = "ID" + str(randint(1000000000, 9999999999))
        return new_id

    def make_bank_id():
        new_bank_id = randint(100000, 999999)
        for i in range(len(profile_list)):
            if len(profile_list) > 0:
                while new_bank_id == profile_list[i].bank_id:
                    new_bank_id = randint(100000, 999999)
        return new_bank_id

    if name == "x":
        name = make_id()

    new_bank_identity = make_bank_id()
    name = Profile(name, new_bank_identity, 10000)
    profile_list.append(name)
    return name


# Code start here! #


jim = make_person("jim")
jim.bank_id = 12345
x = make_person("x")

