from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def operate():
    should_continue = True
    while should_continue:
        drink = input(f"\n\nWhat would you like? ({menu.get_items()}\b) ")
        if drink == "report":
            coffee_maker.report()
            money_machine.report()
        elif drink == "off":
            print("Goodbye 👋 ")
            should_continue = False
        else:
            item = menu.find_drink(drink)
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)


operate()

