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

money = 0


def check_items(type):
    available = True
    if MENU[type]['ingredients']['milk'] > resources['milk']:
        print("Sorry there is not enough milk.")
        available = False
    elif MENU[type]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water.")
        available = False
    elif MENU[type]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee.")
        available = False
    return available


def buy_item(type):
    resources['milk'] -= MENU[type]['ingredients']['milk']
    resources['water'] -= MENU[type]['ingredients']['water']
    resources['coffee'] -= MENU[type]['ingredients']['coffee']
    global money
    money += MENU[type]['cost']


def operate():
    should_continue = True
    while should_continue:
        user_choice = input("\n\nWhat would you like? (espresso/latte/cappuccino)")
        if user_choice in MENU:
            available = check_items(user_choice)
            if available:
                cost = MENU[user_choice]['cost']
                print(f"Please enter the amount shown : {cost}")
                quarters = float(input("Enter the number of quarters : "))
                dimes = float(input("Enter the number of dimes : "))
                nickels = float(input("Enter the number of nickels : "))
                pennies = float(input("Enter the number of pennies : "))
                tot = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
                if tot >= cost:
                    buy_item(user_choice)
                    print(f"Here is your ☕ {user_choice}. Enjoy!")
                    if tot > cost:
                        print(f"Here is ${round(tot - cost, 2)} in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif user_choice == "report":
            print(
                f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g\nMoney: ${money}")
        elif user_choice == "off":
            should_continue = False


operate()
