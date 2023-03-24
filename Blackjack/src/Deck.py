from Card import Card
import random
import numpy as np

class Deck:
    def __init__(self, numdecks=6):
        self.numdecks = numdecks
        self.setupDeck(numdecks)

    def setupDeck(self, numdecks=6):
        self.needToReshuffle = False
        self.cards = []
        self.decksize = numdecks * 52
        for i in range(numdecks):
            for suit in ['Club', 'Spade', 'Heart', 'Diamond']:
                self.cards.append(Card(suit, 'A'))
                for i in range(2, 11):
                    self.cards.append(Card(suit, i))
                self.cards.append(Card(suit,'J'))
                self.cards.append(Card(suit,'Q'))
                self.cards.append(Card(suit,'K'))
        
        self.shuffle()
        #cut card location
        #middle of deck as mean / mu
        #1.5x deck size as standard deviation / sigma
        #10 samples, less will have more variance, more samples will have less variance
        s = np.random.normal(len(self.cards) / 2, 52 * 1.5, 10)
        self.cutcard = int(np.mean(s))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def nextCard(self):
        if len(self.cards) < self.decksize - self.cutcard:
            self.needToReshuffle = True
        return self.cards.pop(0)

    def calculateCount(self):
        count = 0
        for card in self.cards:
            if card.evaluate() >= 2 and card.evaluate() <= 6:
                count -= 1
            if card.evaluate() >= 10:
                count += 1
        return count
    
    def copy(self):
        d = Deck()
        d.cards = self.cards.copy()
        return d

    def onRoundEnd(self):
        setupDeck(self.numdecks)
        print('round end code run')

    def __str__(self):
        for card in self.cards:
            print(card.char, 'of', card.suit)
        return ""
