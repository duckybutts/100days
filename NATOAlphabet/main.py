import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
formattedData = {row.letter:row.code for (index, row) in data.iterrows()}

userInput = input("Enter a word: ").upper()
output = [formattedData[letter] for letter in userInput]
print(output)