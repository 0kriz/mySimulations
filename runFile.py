import company
import profile


def day():
    for i in range(len(profile.profile_list)):
        if profile.profile_list[i].job != "No job":
            profile.profile_list[i].balance = profile.profile_list[i].balance + profile.profile_list[i].salary
            company.jack_food_store.balance = company.jack_food_store.balance - profile.profile_list[i].salary

    company.jack_food_store.import_goods(10)


# Run simulation

print("company balance: " + str(company.jack_food_store.balance))
print("company Product amount: " + str(company.jack_food_store.product_amount))
print("Jim's balance: " + str(profile.jim.balance))
day()
print("")
print("company balance: " + str(company.jack_food_store.balance))
print("company Product amount: " + str(company.jack_food_store.product_amount))
print("Jim's balance: " + str(profile.jim.balance))
