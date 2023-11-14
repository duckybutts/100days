import random

logo = '''

 #     #                                       #####                                            
 ##    # #    # #    # #####  ###### #####    #     # #    # ######  ####   ####  ###### #####  
 # #   # #    # ##  ## #    # #      #    #   #       #    # #      #      #      #      #    # 
 #  #  # #    # # ## # #####  #####  #    #   #  #### #    # #####   ####   ####  #####  #    # 
 #   # # #    # #    # #    # #      #####    #     # #    # #           #      # #      #####  
 #    ## #    # #    # #    # #      #   #    #     # #    # #      #    # #    # #      #   #  
 #     #  ####  #    # #####  ###### #    #    #####   ####  ######  ####   ####  ###### #    # 
                                                                                                                                                                
'''


def checkNumber(userG, compG, attemptsRemaining):
    global won
    if userG > compG:
        print("Too high")
    elif userG < compG:
        print("Too low")
    else:
        print(f"Correct! The number was {compG}!")
        won = True
def play():
    print(logo)
    global won

    # get user attempts
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty == 'easy':
            attemptsRemaining = 10
            break
        elif difficulty == 'hard':
            attemptsRemaining = 5
            break
        else:
            print("Invalid selection. Please enter 'easy' or 'hard'.")

    print("I'm thinking of a number between 1 and 100.")
    computerNumber = random.randint(1, 100)

    while attemptsRemaining > 0 and won == False:
        userGuess = int(input("Guess a number: "))
        attemptsRemaining -= 1
        checkNumber(userGuess, computerNumber, attemptsRemaining)
        if attemptsRemaining <= 0:
            print(f"You're out of attempts. The correct number was {computerNumber}.")
        elif attemptsRemaining > 0 and won == True:
            print(f"Good job!!!")
        else:
         print(f"You have {attemptsRemaining} attempts remaining.")

playing = True
print("Welcome to the Number Guessing Game!")
while playing:
    won = False  # initialize
    play()
    cont = input("Would you like to play again? Type 'Y' or 'N'  ")
    if cont.upper() == 'N':
        playing = False