

# Run Simulation
import business_struct
import person
import environment


# For data visualisation
count_dead = 0
dead_per_day_log = []


# construct simulation
def day(days):
    count = 0
    for i in range(days):
        # all lands grow crops, max amount = 2x land size
        for r in range(len(environment.land)):
            environment.land[r].day()
            if environment.land[r].storage_ready >= (2*environment.land[r].size):
                environment.land[r].storage_ready = (2*environment.land[r].size)
        # animals eat, starve, die
        for z in range(len(environment.animals)):
            environment.animals[z].hunger()
        for cow in range(len(environment.cows)):
            if environment.grass_land[0].storage_ready > 0:
                environment.cows[cow].eat(environment.grass_land[0])
        for wolf in range(len(environment.wolfs)):
            if len(environment.cows) > 0:
                if environment.cows[0].health > 0:
                    environment.wolfs[wolf].attack(environment.cows[0])
                if environment.cows[0].health <= 0:
                    environment.wolfs[wolf].eat(environment.cows[0])
                    environment.cows[0].die()
        for z in range(len(environment.animals)):
            if environment.animals[z].food < 1:
                environment.animals[z].starve()
            if environment.animals[z].health <= 0:
                environment.animals[z].die()
        # all businesses import goods from suppliers or land-field, convert raw products to ready products, pay workers
        for r in range(len(business_struct.businesses)):
            business_struct.businesses[r].productivity()
            business_struct.businesses[r].import_all_goods()
            business_struct.businesses[r].pay_worker()
        # population eat, buys food, starve, die
        for j in range(len(person.population)):
            try:
                person.population[j].eat()
                person.population[j].buy_food(1)
                person.population[j].hunger()
                if person.population[j].food < 1:
                    person.population[j].starve()
                if person.population[j].health < 1:
                    person.population[j].die()
                    global count_dead
                    count_dead += 1
            except IndexError:
                pass

        dead_per_day_log.append(count_dead)
        count_dead = 0
        count = count + 1


# construct simulation foundation
environment.land_generator("grass", 100)
environment.land[0].storage_ready = 100
person.person_generator(10)
business_struct.farm = business_struct.business_generator("Timmy Farm", 0, 5000, "corn", 20, "farmer")
business_struct.farm.hire(3, person.population)
business_struct.bakery = business_struct.business_generator("Joe's Bread", 0, 1000, "bread", 15, "baker")
business_struct.bakery.hire(6, person.population)
business_struct.farm.resource_source("wheat")
business_struct.bakery.resource_source("Timmy Farm")
person.all_set_food_store() # set after businesses is constructed
environment.cow = environment.Cow("cow", "123", "cow", 100, 5, 100, 10)
environment.animals.append(environment.cow)
environment.cows.append(environment.cow)
environment.wolf = environment.Wolf("wolf", 234, "wolf", 88,  17, 100, 10)
environment.animals.append(environment.wolf)
environment.wolfs.append(environment.wolf)


######

# Simulation start
days_simulated = 45
day(days_simulated)

