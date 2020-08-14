# Read me

To DO
- build person class*
- build Business Struct (BusinessStruct)*
- build farm land (Environment)*
    - crops, amount, growth rate/day()
- build farm (BusinessStruct)*
    - storage, import, sell, employee, salary, balance*
- build bakery (BusinessStruct)*
- make all people buy food, eat; if not food, reduce health every day and kill if health == 0*
- make "Animal" class have the ability to eat, drink, multiply,*
- define a cow as a child of "Animal"*
- make the simulation data visual in matplotlib*
- learn basics Method Resolution Order (MRO)*
- animal the ability to die*
- make wolf be able to kill cow, eat cow if killed and find another cow to kill if cow has no more food. line 29-32 RunSim






Program structure:
- all person class objects and child classes will be located in "person.py"
- all business class objects and child classes will be located in "businessStruct.py"
- all environment classes, objects and child classes will be located in "Environment.py"
- RunSim.py only have "day(days)" function and only executes methods and functions outside of "day(days)""


BusinessStruct.py can:
- create a business with attributes: (self, name, employees, balance, product) (class Business)
- hire and fire employees (hire) (fire)
- hire update persons job and salary attribute
- make partnership with land or other businesses (resource_source)
- import goods from a partner's "ready storage" (import_all_goods)
- convert raw material to ready products based on how many people hired (productivity).


Person.py can:
- create a person class with attributes (self, identity, name, gender, health, food, water, money, job, salary) (class Person)
- create x amount of people (person_generator)
- person_generator generate all parameters, some parameters are random with a redundancy checker to prevent duplicate person objects.
- can make all people set their food store to on store (all_set_food_store)
- person can eat (eat)
- person can set food store to buy food (set_food_store)
- person can buy food (buy_food)
- person can eat if it has food
- person can reduce its food (simulate hunger)
- person can starve if it has no food



environment.py can:
- construct land class with different ground types and different growth rates depending on ground_type
- land object accumulate resources over time (day(days))
- construct animal class
- animal can eat from a food source (lan or other animal)
- animal can drink
- animal can reduce its food (simulate hunger)
- animal can starve
- animal can multiply
- construct predator animal type
- construct cow class (inherit animal)
- construct wolf class (inherit predator)

RunSim.py can:
- simulate growth of all grounds from ground object's growth rate, with max cap at 2x ground size
- auto produce and import goods between land and companies.
- pay workers
- make people eat, buy food starve and die if no health
- make cow objects eat
- make all animals starve if no food
- collects all people who die to use for data visualisation