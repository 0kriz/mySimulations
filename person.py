

# Person
import random
from random import randint

Male_names = ["Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason",
              "Logan", "Alexander", "Ethan", "Jacob", "Michael", "Daniel", "Henry", "Jackson",
              "Sebastian", "Aiden", "Matthew", "Samuel", "David", "Joseph", "Carter", "Owen",
              "Wyatt", "John", "Jack", "Luke", "Jayden"]

Female_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper",
                "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila",
                "Aria", "Scarlett", "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla",
                "Riley", "Zoey", "Nora"]

population = []
dead = []


def person_generator(amount):
    for i in range(amount):
        id = "id" + str(randint(1000000, 9999999))
        for i in range(len(population)):
            if id == population[i].identity:
                id = "id" + str(randint(1000000, 9999999))
        male_female = random.choice(["male", "female"])
        if male_female == "male":
            name = random.choice(Male_names)
        else:
            name = random.choice(Female_names)
        id = Person(id, name, male_female, 100, 25, 25, 100, "no job", 0)
        population.append(id)


def all_set_food_store():
    for i in range(len(population)):
        population[i].set_food_store("Joe's Bread")


class Person:
    def __init__(self, identity, name, gender, health, food, water, money, job, salary):
        self.identity = identity
        self.name = name
        self.gender = gender
        self.health = health
        self.food = food
        self.water = water
        self.money = money
        self.job = job
        self.salary = salary
        self.food_store = "No food store"

    def eat(self):
        if self.food > 0:
            self.food = self.food - 1
        else:
            self.health = self.health - (self.health/10)

    def hunger(self):
        self.food -= 3

    def starve(self):
        self.health -= 10

    def die(self):
        dead.append(self)
        population.remove(self)

    def buy_food(self, amount):
        if self.money > amount*3 and self.food_store != "No food store":
            import business_struct
            if self.food_store.storage_ready > amount:
                self.food_store.storage_ready = self.food_store.storage_ready - amount
                self.food_store.balance = self.food_store.balance + amount*3
                self.food = self.food + amount
                self.money = self.money - amount*3

    def set_food_store(self, store_name):
        import business_struct
        for i in range(len(business_struct.businesses)):
            if business_struct.businesses[i].name == store_name:
                self.food_store = business_struct.businesses[i]

