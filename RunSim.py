# Run Simulation

import business_struct
import person
import environment


# construct simulation


def day(days):
    count = 1
    for i in range(days):
        # all lands grow crops, max amount = 2x land size
        for r in range(len(environment.land)):
            environment.land[r].day()
            if environment.land[r].storage_ready >= (2*environment.land[r].size):
                environment.land[r].storage_ready = (2*environment.land[r].size)
        # all businesses import goods from suppliers/lands, convert raw products to ready products, pay workers
        for r in range(len(business_struct.businesses)):
            business_struct.businesses[r].productivity()
            business_struct.businesses[r].import_all_goods()
            business_struct.businesses[r].pay_worker()
        # population eat, buys food
        for j in range(len(person.population)):
            try:
                person.population[j].eat()
                person.population[j].buy_food(1)
                if person.population[j].health < 1:
                    print(person.population[j].name + " is dead!")
                    del person.population[j]
            except IndexError:
                pass
        count = count + 1


# construct simulation foundation
environment.land_generator("wheat", 100)
person.person_generator(10)
business_struct.farm = business_struct.business_generator("Timmy Farm", 0, 5000, "corn", 20, "farmer")
business_struct.farm.hire(3, person.population)
business_struct.bakery = business_struct.business_generator("Joe's Bread", 0, 1000, "bread", 15, "baker")
business_struct.bakery.hire(6, person.population)
business_struct.farm.resource_source("wheat")
business_struct.bakery.resource_source("Timmy Farm")
person.all_set_food_store() # set after businesses is made


# Simulation start
day(105)










