alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

# ---------------------------FUNCTION ---------------------------
quitProgram = False
def cesarCipher (text, shift, instructions):
    newString = ""
    instructions = instructions.lower()
    if instructions == "decode" or instructions == "encode":
        for i in range(len(text)):
            char = text[i]
            if char in alphabet:
                oldPosition = alphabet.index(text[i])
                if instructions == "encode":
                    newPosition = (oldPosition + shift) % len(alphabet)
                elif instructions == "decode":
                    newPosition = (oldPosition - shift) % len(alphabet)
                newLetter = alphabet[newPosition]
                newString += newLetter
            else:
                newString += char
        print(f"The {instructions}d text is {newString}")
    else:
        print("Invalid Selection, please select either encode or decode.")



# ---------------------------PROGRAM ---------------------------

while not quitProgram:
    instructions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesarCipher(text, shift, instructions)
    again = input("Would you like to play again? Type 'yes' or 'no':\n")
    if again == "no":
        quitProgram = True
    else:
        quitProgram = False