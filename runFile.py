import company
import profile
days = 0
month = 0
new_month = False


def day():
    global days
    global month
    global new_month

    if days != 31:
        new_month = False

    days += 1
    if days == 31:
        new_month = True
        print("new_month = true")
        month += 1
        days = 0

    for i in range(len(profile.profile_list)):
        if profile.profile_list[i].job != "No job":
            profile.profile_list[i].balance = profile.profile_list[i].balance + profile.profile_list[i].salary
            company.jack_food_store.balance = company.jack_food_store.balance - profile.profile_list[i].salary
    company.jack_food_store.import_goods(10)

    for i in range(len(profile.profile_list)):
        profile.profile_list[i].food_consumption()
        if profile.profile_list[i].loan and new_month:
            profile.profile_list[i].pay_loan(company.lenders_bank)


# Run simulation

days_simulated = 32
print(company.lenders_bank.balance)
print(profile.jim.balance)
company.lenders_bank.lend_money(profile.jim, 25000)

count = 0
for i in range(days_simulated):
    day()
    count += 1
    print("day: " + str(count))

print("")
print(profile.jim.balance)
print(company.lenders_bank.balance)


