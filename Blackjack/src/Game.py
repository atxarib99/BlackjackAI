from Player import Player
from Deck import Deck
class Game:
    def __init__(self, numplayers=3):
        self.players = []
        self.dealer = Player("Dealer")
        for i in range(numplayers):
            self.players.append(Player(name=i))
        self.deck = Deck()
    
    def addPlayer(self, player):
        self.players.append(player)

    def startRound(self):
        self.askForBets()
        self.drawCards()
        self.handlePlayers()
        self.handleDealer()
        for player in self.players:
            print("Player " + str(player.name) + " cards: " + str(player.cards))
            print("Player " + str(player.name) + " value: " + str(player.evaluate()))
        
        print("Dealer" + " cards: " + str(self.dealer.cards))
        print("Dealer" + " value: " + str(self.dealer.evaluate()))

    def askForBets(self):
        self.playerBets = [0] * len(self.players)
        for player,index in zip(self.players, range(len(self.players))):
            #todo: error checking here. Cant bet more than u have
            bet = input("Player " + str(player.name) + " enter how much you want to bet...")
            self.playerBets[index] = int(bet)
    
    def drawCards(self):
        #players
        for player in self.players:
            player.hit(self.deck)
        #dealer hidden
        self.dealer.hiddencard = self.deck.nextCard()
        #players
        for player in self.players:
            player.hit(self.deck)
        #dealer
        self.dealer.hit(self.deck)
    
    def handlePlayers(self):
        for player in self.players:
            while True:
                print("Player " + str(player.name) + " cards: " + str(player.cards))
                print("Player " + str(player.name) + " value: " + str(player.evaluate()))
                choice = input("Player " + str(player.name) + " your move [hit,stand]...")
                if choice == "hit":
                    player.hit(self.deck)
                    if player.evaluate() > 21:
                        print("Player " + str(player.name) + " cards: " + str(player.cards))
                        print("Player " + str(player.name) + " value: " + str(player.evaluate()))
                        print("Bust!")
                        break
                if choice == "stand":
                    break
    
    def handleDealer(self):
        self.dealer.cards.append(self.dealer.hiddencard)
        while self.dealer.evaluate() < 17:
            self.dealer.hit(self.deck)
        print("Dealer value:", self.dealer.evaluate())