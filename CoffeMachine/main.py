from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

options = ["off", "report", "espresso", "latte", "cappuccino"]
drinks = options[2:]
finish = False
money = 0


def is_resource_available(drink):
    is_enough = True
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry. There is not enough {ingredient}.")
            is_enough = False
    return is_enough


def process_transaction():
    profit = 0
    print("Insert your coins, please.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    inserted_money = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if inserted_money >= MENU[option]["cost"]:
        change = inserted_money - MENU[option]["cost"]
        profit = inserted_money - change
        print(f"Here is ${change} in change.")
    else:
        print("Not enough money. Your money has been refunded.")
    return profit


def make_coffee(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy it!")


print(logo)

while not finish:
    option = ""
    while option not in options:
        option = input("What would you like?   ")
        if option not in options:
            print("This option is not available. Try again")

    if option == "off":
        print("Coffee machine will turn off...")
        finish = True
    elif option == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"money: ${money}")
    elif option in drinks:
        if is_resource_available(option):
            new_money = process_transaction()
            if new_money > 0:
                money += new_money
                make_coffee(option)
        else:
            print("We could not process your request.")
