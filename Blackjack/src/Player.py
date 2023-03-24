from abc import ABC, abstractmethod
from Card import Card
class Player:
    def __init__(self, name, starting_chips=100):
        #an array of the cards currently held by the user
        self.cards = []
        self.chips = starting_chips
        self.name = name
        self.hiddencard = Card('Heart', 'A')
        self.initagain()

    #init for each type of player
    @abstractmethod
    def initagain():
        pass
    
    def hit(self, deck):
        self.cards.append(deck.nextCard())
        #bust
        if self.evaluate() > 21:
            #prob need some form of end turn mechanism here
            return False

    def stand(self):
        #end turn mech
        return True

    #each player/agent will implement this uniquely
    @abstractmethod
    def askForBets(self):
        pass

    #each player will define their strategy when asked
    @abstractmethod
    def strategy(self):
        pass

    
    def evaluate(self):
        #aces are always handed as 11 unless over
        sorted_cards = sorted(self.cards, key=lambda x: x.evaluate())
        value = 0
        index = 0
        for card in sorted_cards:
            index+=1 
            #this misbehaves with multiple aces (4,6,A,A)
            if card.char == 'A':
                #if value + 11 > 21 - (aces left)
                if value + 11 > 21 - (len(sorted_cards) - index):
                    value += 1
                else:
                    value += 11
            else:
                value += card.evaluate()

        return value


