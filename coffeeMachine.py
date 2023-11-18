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


def makeBeverage(drink, resources):
    ingredientsDic = drink["ingredients"]
    water = ingredientsDic["water"]
    resources["water"] = resources["water"] - water
    if drink != MENU["espresso"]:
        milk = ingredientsDic["milk"]
        resources["milk"] = resources["milk"] - milk
    coffee = ingredientsDic["coffee"]
    resources["coffee"] = resources["coffee"] - coffee

    for resource in resources.values():
        if resource < 0:
            print("Sorry, not enough resources in the machine.")
            return False
    return True

def processPayment(q, d, n, p):
    """ returns double 'money processed' """
    moneyProcessed = 0
    for i in range(0, q):
        moneyProcessed += .25
    for i in range(0, d):
        moneyProcessed += .10
    for i in range(0, n):
        moneyProcessed += .5
    for i in range(0, p):
        moneyProcessed += .01

    return round(moneyProcessed,2)

drink = input("What would you like? (espresso/ latte/ cappuccino): ")
drink = drink.capitalize()

# take a payment
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))

payments = processPayment(quarters, dimes, nickels, pennies)

if drink == "Cappuccino":
    beveragePrice = MENU["cappuccino"].get("cost")
    if payments > beveragePrice:
        print(f"You input: ${payments}")
        made = makeBeverage(MENU["cappuccino"], resources)
    else:
        print(f"Not enough money input. You have been refunded ${payments}")
elif drink == "Latte":
    beveragePrice = MENU["latte"].get("cost")
    if payments > beveragePrice:
        print(f"You input: ${payments}")
        made = makeBeverage(MENU["latte"], resources)
    else:
        print(f"Not enough money input. You have been refunded ${payments}")
elif drink == "Espresso":
    beveragePrice = MENU["espresso"].get("cost")
    if payments > beveragePrice:
        print(f"You input: ${payments}")
        made = makeBeverage(MENU["espresso"], resources)
    else:
        print(f"Not enough money input. You have been refunded ${payments}")
else:
    print("Invalid Selection.")

if not made:
    print("Not enough resources in the machine. Sorry!")

print(f"Your {drink} is ready! Your change is: ${round((payments - beveragePrice), 2)}")

