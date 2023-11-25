logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     |  |     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   |_|  | || |    | || |    | || |    | |       | || |  / .'   |_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   | ____ |   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  | `.___.'|  | || | _| |    | |_ | || |   _| |__/ |  | || |  | `.___.'|  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# create a dictionary where the keys are the operations,and the value is the name of the function
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number? "))
    for operation in operations:
        print(operation)

    selection = input("\n Pick an operation from the selections above? ")
    num2 = float(input("What is the second number? "))

    functionChoice = operations[selection]
    answer = functionChoice(num1, num2)
    print(f"{num1} {selection} {num2} = {answer}")

    calculating = True

    while calculating:
        cont = input(f"Would you like to continue calculating with {answer}? Y or N? ")
        if cont.upper() == "Y":
            num1 = answer
            selection = input("\nPick a new operation. ")
            num2 = float(input("Enter another number. "))
            functionChoice = operations[selection]
            answer = functionChoice(num1, num2)
            print(f"{num1} {selection} {num2} = {answer}")
        else:
            calculator()
            calculating = False

calculator()