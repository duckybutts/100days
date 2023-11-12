import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |           | |   | |          | |  (_)          | |   
|( || ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| |  ||K /|  |     | '_ || || _` |/ __| |/ / |/ _` |/ __| |/ /
|  || | /  | |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| |  / |     |_.__/|_||__,_||___|_||_| ||__,_||___|_||_|
      |  |/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playerCards = 0
playerScore = 0
computerCards = 0
computerScore = 0
computerCardList = []
playerCardList = []


def getNewCard(cards):
    """Gets random card value from cards list and returns it's value"""
    index = random.randint(0, 12)
    card = cards[index]
    return card

def countCards(card_list):
    aces = 0
    score = 0
    for i in range(0, len(card_list)):
        if card_list[i] == 11:
            aces += 1
        score += card_list[i]
        while aces > 0 and score > 21:
            aces -= 1
            score -= 10
    return score

def addCard(cards, list):
    newCard = getNewCard(cards)
    list.append(newCard)


playing = True

while playing:
    selection = input("Do you want to play blackjack? Y or N? ").strip()
    if selection.upper() == 'Y':
        print(logo)

        while playerCards < 2:  # get player cards
            addCard(cards, playerCardList)
            playerCards += 1

        while computerCards < 2:  # get computer cards
            addCard(cards, computerCardList)
            computerCards += 1

            computerScore = countCards(computerCardList)

        while computerScore < 17:  # ensure dealer pulled up to 17
            addCard(cards, computerCardList)
            computerCards += 1
            computerScore = countCards(computerCardList)


        print(f"Your cards are: {playerCardList}")
        print(f"Computer's cards are: [{computerCardList[0]}, X]")

        playerScore = countCards(playerCardList)
        anotherCard = True

        while anotherCard:
            selection = input("Would you like another card? Y or N? ")
            if selection.upper() == "N":
                anotherCard = False
            else:
                newCard = getNewCard(cards)
                playerCardList.append(newCard)
                playerScore = countCards(playerCardList)
                print(f"Your cards are: {playerCardList}")
                if playerScore > 21:
                    anotherCard = False

        print(f"Your cards: {playerCardList}")
        print(f"Dealer's cards: {computerCardList}")
        if computerScore > 21:
            print(f"The dealer has a score of {computerScore}. They busted! You win! ")
        elif playerScore > 21:
            print(f"Your score is {playerScore}. That's over 21! You lose. ")
        elif playerScore < computerScore:
            print(f"Your score is {playerScore}. That's less than {computerScore}! You lose. ")
        elif playerScore > computerScore:
            print(f"Your score is {playerScore}. That's more than {computerScore}! You win! ")
        else:
            print(f"Your score is: {playerScore}. The computer scored: {computerScore}! It's a draw! ")

        playerCards = 0
        playerScore = 0
        computerCards = 0
        computerScore = 0
        computerCardList = []
        playerCardList = []

    else:
        playing = False