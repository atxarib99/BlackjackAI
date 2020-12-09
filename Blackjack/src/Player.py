class Player:
    def __init__(self, starting_chips=100):
        #an array of the cards currently held by the user
        self.cards = []
        self.chips = starting_chips
    
    def hit(self, deck):
        self.cards.append(deck.nextCard())
        #bust
        if self.evaluate() > 21:
            #prob need some form of end turn mechanism here
            return False

    def stand(self):
        #end turn mech
        return True
    
    def evaluate(self):
        #dynamic aces might need to be handed here
        value = 0
        for card in self.cards:
            value += card.evaluate()
        return value
