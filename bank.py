from random import random, randint


class Profile:
    def __init__(self, name, bank_id, balance):
        self.name = name
        self.bank_id = bank_id
        self.balance = balance

    def get_info(self):
        print("Person name: " + self.name)
        print("Person's bank ID: " + str(self.bank_id))
        print("Persons's available balance: " + str(self.balance))


def transactions(user1, user2, amount):
    user1.balance = user1.balance + amount
    user2.balance = user2.balance - amount


profile_list = []


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


# Code start here! #


for i in range(100):
    new_identity = make_id()
    new_bank_identity = make_bank_id()
    new_identity = Profile(new_identity, new_bank_identity, 10000)
    profile_list.append(new_identity)

for i in range(len(profile_list)):
    print("object name: " + profile_list[i].name)
    print("object bank ID: " + str(profile_list[i].bank_id))
    print("object bank balance: " + str(profile_list[i].balance))
    print("\n")


