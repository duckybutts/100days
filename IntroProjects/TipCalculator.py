print("------------------------------")
print("Welcome to the tip calculator!")
print("------------------------------")
total = input("What was the total bill? ")
percentage = input("What percentage tip would you like to leave? ")
split = input("How many people are paying? ")

amount = int(percentage)/100
amount = amount * int(total)

if (int(split) == 1):
    print(f"You should pay: {amount}")

else:
    amount = round((amount/int(split)),2)
    print(f"You each should pay: {amount}")