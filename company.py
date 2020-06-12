from random import random, randint
import profile


class Company:
    def __init__(self, company_name, store_type, products, product_amount, balance):
        self.company_name = company_name
        self.store_type = store_type
        self.products = products
        self.product_amount = product_amount
        self.balance = balance
        self.price = 50
        self.employee = []

    def hire(self, person_name):
        self.employee.append(person_name)
        person_name.job = "cashier"
        person_name.salary = 1000


class Store(Company):

    # import price = 20
    def import_goods(self, amount):
        self.product_amount = self.product_amount + amount
        self.balance = self.balance - (amount * 20)

    def sell_goods(self, amount, person):
        self.product_amount = self.product_amount - amount
        self.balance = self.balance + (amount * self.price)
        person.balance = person.balance - (amount * self.price)
        person.food = person.food + amount


class Bank(Company):
    loans = {}

    def lend_money(self, person, amount):
        if person.salary != "No salary" and ((person.salary * 235) >= (amount * 5)):
            if self.balance > (amount * 5):
                person.loan = amount
                person.balance = person.balance + amount
                self.balance = self.balance - amount
                loan = [person.name, amount]
                Bank.loans[person.bank_id] = loan


# code start here!


jack_food_store = Store("jacks food store", "food store", "food", 50, 50000)
lenders_bank = Bank("lenders bank", "bank", "currency", 10000000, 10000000)
lenders_bank.hire(profile.jim)







