from menu import MENU, resources

profit = 0

def print_resources():
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.capitalize()}: {resources[resource]}g")
    print(f"Money: ${profit}")

def check_resources(supplies, menu):
    for key in menu:
        if supplies.get(key, 0) < menu[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def resource_reduction(supplies_1, menu_1):
    for key_1 in menu_1:
        supplies_1[key_1] -= menu_1[key_1]

def insert_coins(menu_2):
    print("Please insert coins")

    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies? : "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if total >= menu_2['cost']:
        change = round((total - menu_2['cost']), 2)
        print(f"Here is {change} in change")
        global profit
        profit += menu_2['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def main_part(choice):
    if choice == "off":
        exit()
    elif choice == "report":
        print_resources()
    elif choice in MENU:
        enough_resources = check_resources(resources, MENU[choice]['ingredients'])
        if enough_resources:
            enough_coins = insert_coins(MENU[choice])
            if enough_coins:
                resource_reduction(resources, MENU[choice]['ingredients'])
                print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("Your choice should be: espresso, latte, cappuccino, report or off.")
def game():
    choice_1 = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while choice_1 != "off":
        main_part(choice_1)
        choice_1 = input("What would you like? (espresso/latte/cappuccino): ").lower()

game()

