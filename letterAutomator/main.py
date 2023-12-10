# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# want to read the starting letter
with open("Input/Letters/starting_letter.txt", mode = "r") as file:
    template = file.read()
with open("Input/Names/invited_names.txt", mode = "r") as file:
    names = file.readlines()

for name in names:          # for n in list
    name = name.strip()
    placeHolder = template  # Create a copy of starting letter

    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode = "w") as file:
        file.write(placeHolder.replace("[name],", f"{name},"))


