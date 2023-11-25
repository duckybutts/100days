from os import system, name

logo = '''
                         ___________
                         |         |
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                       .-------------.
                      /_______________|
'''

print(logo)


# ################### Functions #################### #

def clear():
    _ = system('clear')


def calcHighestBidder(b):
    highestBid = 0
    for bidder in bidders:
        amount = int(bidders[bidder])
        if amount > highestBid:
            highestBid = amount
            winner = bidder
    print(f"The winner is {winner}, with the highest bid of {highestBid}!")


# ################### Program #################### #

bidding = True
bidders = {}  # initialize dictionary

while bidding:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders[name] = bid  # add new entry
    cont = input("Is there another bidder? Y or N? : ")
    if cont.upper() == "Y":
        clear()
    else:
        calcHighestBidder(bidders)
        bidding = False
