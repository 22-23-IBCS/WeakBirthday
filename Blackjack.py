import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getCard(self):
        return [self.suit, self.name]

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for s in suits:
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)

                C = Card(s, name)
                self.cards.append(C)

    def getCards(self):
        return self.cards

    #this function deals cards randomly
    def dealCard(self):
        newCard = random.choice(self.cards)
        self.cards.remove(newCard)
        return newCard

def calcHandValue(hand):
    total = 0
    for h in hand:
        name = h[1]
        if name == "Ace":
        #Ace is 11 or 1, and this changes it based on the value of the hand
            total = total + 11
            if total > 21:
                total = total - 10
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
        else:
            total = total + int(name)
        
    return total
        

def main():

    print("Welcome to Blackjack!\n") 

    D = Deck()

    #these functions define the hands of dealer and user
    x = D.dealCard().getCard()
    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    dealerHand = [D.dealCard().getCard(), "x"]
    
    print("Dealer hand: ")
    print(dealerHand)
    print("")
    print(userHand)
    print("Your hand's value is: " + str(calcHandValue(userHand)))
    print("")

    #this section offers choice input of hit or stand, and deals a card if hit is selected
    while True:
        option = input("Type 1: Hit  or 2: Stand\n")
        if option == "1":
            userHand.append(D.dealCard().getCard())
            print("")
            print(userHand)
            print("Your hand's value is: " + str(calcHandValue(userHand)))
            print("")
            if calcHandValue(userHand) > 21:
                print("You Bust!")
                break
            if calcHandValue(userHand) == 21:
                break

        else:
            break

    #this section displays the hand value after each card is drawn
    print("")
    print("Dealer hand: ")
    print(dealerHand)
    print("Dealer hand's value is: " + str(calcHandValue(dealerHand)))
    print("")
    
    while True:
    #this calculates and displays the values of the hand after each hit, and accounts for busts
        if calcHandValue(dealerHand) < 17 and calcHandValue(userHand) <= 21:
            print("Dealer hits!\n")
            dealerHand.append(D.dealCard().getCard())
            print("Dealer hand:")
            print(dealerHand)
            print("Dealer hand's value is: " + str(calcHandValue(dealerHand)))
            print("")
        else:
        #this section tests the values when dealer stands and determines the winner
            print("Dealer stands!\n")
            if calcHandValue(dealerHand) < calcHandValue(userHand) and calcHandValue(userHand) <= 21:
                print("You win!")
            elif calcHandValue(dealerHand) == calcHandValue(userHand):
                print("Tie!")
            else:
                print("Dealer win!")
            break
        if calcHandValue(dealerHand) > 21:
        #this section checks if dealer goes over 22
            print("Dealer bust!")
            print("You win!")
            break
        
        
        
        

if __name__ == "__main__":
    main()
