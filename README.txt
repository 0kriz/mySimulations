# Read me

To DO
- build person class*
- build Business Struct (BusinessStruct)*
- build farm land (Environment)*
    - crops, amount, growth rate/day()
- build farm (BusinessStruct)*
    - storage, import, sell, employee, salary, balance*
- build bakery (BusinessStruct)*
- make all people buy food, eat; if not food, reduce health every day and kill if health == 0

Program structure:
- all person class objects and child classes will be located in "person.py"
- all business class objects and child classes will be located in "businessStruct.py"
- all environment classes, objects and child classes will be located in "Environment.py"
- RunSim.py only executes methods and functions


BusinessStruct.py can:
- create a business with attributes: (self, name, employees, balance, product)
- hire and fire employees
- hire update persons job and salary attribute
- import goods from a partner's "ready storage"
- convert raw material to ready products based on how many people hired.


Person.py can:
- create a person class with attributes (self, identity, name, gender, health, food, water, money, job, salary)
- create x amount of people with the person_generator function
- person_generator generate all parameters, some parameters are random with a redundancy checker to prevent duplicate person objects.


environment.py can:
- construct land class with different ground types and different growth rates depending on ground_type
- land object accumulate resources over time (day(days))
- construct animal class

RunSim.py can:
- simulate growth of all grounds from ground object's growth rate, with max cap at 2x ground size
- auto produce and import goods between land and companies.