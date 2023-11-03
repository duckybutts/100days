import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



computerChoice = random.randint(0,2) #choose rock paper or scissors
playerChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors: ")

if playerChoice == "0":
    playerChoice = rock
elif playerChoice == "1":
    playerChoice = paper
elif playerChoice == "2":
    playerChoice = scissors
else:
    print("Invalid input.")


if computerChoice == 0:
    computerChoice = rock
elif computerChoice == 1:
    computerChoice = paper
elif computerChoice == 2:
    computerChoice = scissors

# if same
if computerChoice == playerChoice:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("It's a tie!")

if computerChoice == rock and playerChoice == scissors:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("Computer Wins!")

if computerChoice == rock and playerChoice == paper:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("You Win!")

if computerChoice == scissors and playerChoice == paper:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("Computer Wins!")

if computerChoice == scissors and playerChoice == rock:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("You Win!")

if computerChoice == paper and playerChoice == rock:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("Computer Wins!")

if computerChoice == paper and playerChoice == scissors:
    print(playerChoice)
    print("Computer chose:")
    print(computerChoice)
    print("You Win!")