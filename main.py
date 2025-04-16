from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    initial_prompt = input("What would you like ? (latte | espresso | cappuccino)\n").lower()
    chosen_drink = menu.find_drink(initial_prompt)

    if not chosen_drink is None:
        drink_cost = chosen_drink.cost
        is_resources_enough = coffee_maker.is_resource_sufficient(chosen_drink)
        if is_resources_enough:
            drink_payment = money_machine.make_payment(drink_cost)
            if drink_payment:
                print("Payment successful")
                coffee_maker.make_coffee(chosen_drink)
            elif not drink_payment:
                print("Payment unsuccessful")
        elif not is_resources_enough:
            print("Not enough resources")

    if initial_prompt == "off":
        for number in range(20):
            print("\n")
    elif initial_prompt == "report":
        coffee_maker.report()


coffee_machine()
