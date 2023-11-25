from gameData import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ // _ // ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_//__, /_/ /_//___/_/     
   / /  /____/_      _____  _____
  / /   / __ / | /| / / _ // ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____//____/|__/|__//___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

gameOver = False
score = 0

choiceA = random.choice(list(data))
choiceB = random.choice(list(data))
while choiceA == choiceB:
    choiceB = random.choice(list(data))

while not gameOver:
    print(logo)
    if score >= 1:
        print: print(f"Correct! Your score is currently {score}!")
    print(f"Compare : {choiceA["name"]}, a {choiceA["description"]} from {choiceA["country"]}")
    print(vs)
    print(f"Against : {choiceB["name"]}, a {choiceB["description"]} from {choiceB["country"]}")
    guess = input("Who has more followers? Type 'A' or 'B': ")

    if int(choiceA["follower_count"]) > int(choiceB["follower_count"]):
        larger = "A"
        winner = choiceA
    else:
        larger = "B"
        winner = choiceB

    if guess.upper() == larger:
        score += 1
        choiceA = winner
        choiceB = random.choice(list(data))
        if choiceB == choiceA:
            choiceB = random.choice(list(data))
    else:
        print(f"WRONG!. Your final score was: {score}.")
        gameOver = True

