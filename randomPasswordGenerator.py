import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

letterLen = nr_letters
symLen = nr_symbols
numLen = nr_numbers

for letter in range(0, letterLen):
    index = random.randint(0, len(letters)-1)
    newLetter = letters[index]
    password += str(newLetter)
for letter in range(0, symLen):
    index = random.randint(0, len(symbols)-1)
    newSymbol = symbols[index]
    password += str(newSymbol)
for letter in range(0, numLen):
    index = random.randint(0, len(numbers)-1)
    newNum = numbers[index]
    password += str(newNum)

shuffle = list(password)
random.shuffle(shuffle)
password = ''.join(shuffle)

print(password)


