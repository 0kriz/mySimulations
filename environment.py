

# Environment
from random import randint

land = []
grass_land = []
animals = []
wolfs = []
cows = []
animals_dead = []


def land_generator(ground_type, size):
    ground_id = Ground("id" + str(randint(100000, 999999)), ground_type, size)
    ground_id.set_grow_rate()
    land.append(ground_id)
    grass_land.append(ground_id)


# ground type can only be ["grass", "water", "rock", "corn", "wheat"]
class Ground:
    def __init__(self, id, ground_type, size):
        self.id = id
        self.ground_type = ground_type
        self.size = size
        self.growth_rate = 0

        self.storage_ready = 0

    def set_grow_rate(self):
        if self.ground_type == "grass" or self.ground_type == "water" or self.ground_type == "rock":
            self.growth_rate = 0.1
        elif self.ground_type == "corn" or self.ground_type == "wheat":
            self.growth_rate = 0.2

    def day(self):
        self.storage_ready = self.storage_ready + (self.size*(1+self.growth_rate)-self.size)


class Animal:
    def __init__(self, specie, identity, name, health, strength, food, water):
        self.specie = specie
        self.identity = identity
        self.name = name
        self.health = health
        self.strength = strength
        self.food = food
        self.water = water
        self.food_preference = None
        self.drink_preference = water
        self.food_type = None
        self.amount_of_meat = None

    def eat(self, food_source):
        try:
            if food_source.ground_type == self.food_preference:
                if food_source.storage_ready > 5:
                    if self.food < 80:
                        self.food += 5
                        food_source.storage_ready -= 5
                else:
                    print("not enough " + str(food_source.ground_type) + " To eat!")
        except AttributeError:
            pass

        try:
            if food_source.food_type == self.food_preference:
                if food_source.amount_of_meat > 5:
                    if self.food < 80:
                        self.food += 5
                        food_source.amount_of_meat -= 5
                else:
                    print("not enough " + str(food_source.ground_type) + " To eat!")
        except AttributeError:
            pass

    def drink(self, water_source):
        try:
            if water_source.ground_type == self.drink_preference:
                if water_source.storage_ready > 0:
                    if self.water < 60:
                        self.water += 5
                        water_source.storage_ready -= 5
                else:
                    print("not enough " + str(water_source.product) + " To drink!")
        except AttributeError:
            pass

        try:
            if water_source.product == "water":
                if water_source.storage_ready > 0:
                    self.water += 5
                    water_source.storage_ready -= 5
                else:
                    print("not enough " + str(water_source.product) + " To drink!")
        except AttributeError:
            pass

    def hunger(self):
        self.food -= 3

    def starve(self):
        self.health -= 10

    def die(self):
        if self.health <= 0:
            animals_dead.append(self)
            animals.remove(self)


    def multiply(self, specie, identity, name, health, strength, food, water):
        return type(self)(specie, identity, name, health, strength, food, water)


class Predator(Animal):
    def attack(self, prey):
        prey.health = prey.health - (self.strength * 3)


class Cow(Animal):
    def __init__(self, specie, identity, name, health, strength, food, water):
        super().__init__(specie, identity, name, health, strength, food, water)
        self.food_preference = "grass"
        self.food_type = "meat"
        self.amount_of_meat = 300

    def die(self):
        super().die()
        cows.remove(self)


class Wolf(Predator):
    def __init__(self, specie, identity, name, health, strength, food, water):
        super().__init__(specie, identity, name, health, strength, food, water)
        self.food_preference = "meat"
        self.food_type = "meat"

    def die(self):
        super().die()
        wolfs.remove(self)
