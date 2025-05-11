from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    choice = input("What would you like to drink? (espresso, latte, cappuccino): ")
    if choice == "report":
        maker.report()
        money.report()
    elif choice == "off":
        is_on = False
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)
    else:
        print("You should type: espresso, latte, cappuccino, report or off.")