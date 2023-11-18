from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMachine = CoffeeMaker()

on = True
while on:
    menus = Menu()
    options = menus.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        on = False
    elif choice == "report":
        coffeeMachine.report()
        moneyMachine.report()
    else:
        drink = menus.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMachine.make_coffee(drink)
