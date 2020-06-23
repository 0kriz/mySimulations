from random import randint
# Environment

land = []


def land_generator(ground_type, size):
    ground_id = Ground("id" + str(randint(100000,999999)), ground_type, size)
    ground_id.set_grow_rate()
    land.append(ground_id)


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
    def __init__(self, identity, name, health, strength, ):
        self.identity = identity
        self.name = name
        self.health = health
        self.strength = strength



