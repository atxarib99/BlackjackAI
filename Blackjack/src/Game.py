from Player import Player
from Human import Human
from FixedAgent import FixedAgent
from Deck import Deck
from GameWindow import GameWindow
import os


class Game:
    def __init__(self, numplayers=3):
        self.roundCount = 0
        self.players = []
        self.dealer = Human("Dealer")
        for i in range(numplayers):
            fa = FixedAgent(name=str(i))
            fa.setGame(self)
            self.players.append(fa)

        self.deck = Deck()
        self.window = GameWindow()

    def addPlayer(self, player):
        self.players.append(player)

    def startRound(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        s = ""
        for i in range(int(columns)):
            s += "="
        print(s)
        print("ROUND " + str(self.roundCount))
        if self.deck.needToReshuffle:
            self.deck.setupDeck()
            print('DECK RESHUFFLED')
        print(s)
        if self.roundCount % 10 == 0:
            print(self.deck.calculateCount())
        self.askForBets()
        self.drawCards()
        print("Dealer cards: " + str(self.dealer.cards))
        self.window.drawGameState(self)
        self.handlePlayers()
        self.handleDealer()
        for player in self.players:
            print("Player " + str(player.name) + " cards: " + str(player.cards))
            print("Player " + str(player.name) + " value: " + str(player.evaluate()))
        
        print("Dealer" + " cards: " + str(self.dealer.cards))
        print("Dealer" + " value: " + str(self.dealer.evaluate()))

        self.window.drawGameState(self, drawBlank=False)
        self.handlePayout()
        self.roundCount += 1

    def askForBets(self):
        for player in self.players:
            print("Player " + player.name + " has " + str(player.chips) + " chips.")
        #remove players with 0 chips
        index = 0
        while index < len(self.players):
            if self.players[index].chips <= 0:
                self.players.remove(self.players[index])
            index+=1

        if len(self.players) == 0:
            print('Game Over!')
            exit(0)

        self.playerBets = [0] * len(self.players)
        for player,index in zip(self.players, range(len(self.players))):
            bet = player.askForBets()
            self.playerBets[index] = bet
            player.chips -= bet
    
    def drawCards(self):
        #reset all cards
        self.dealer.hiddencard = None
        self.dealer.cards.clear()
        for player in self.players:
            player.cards.clear()
        #players
        for player in self.players:
            player.hit(self.deck)
        #dealer hidden
        self.dealer.hiddencard = self.deck.nextCard()
        print(self.dealer.hiddencard)
        #players
        for player in self.players:
            player.hit(self.deck)
        #dealer
        self.dealer.hit(self.deck)
    
    def handlePlayers(self):
        index = -1
        for player in self.players:
            index += 1
            while True:
                self.window.drawGameState(self)
                if player.evaluate() == 21:
                    break
                print("Player " + str(player.name) + " cards: " + str(player.cards))
                print("Player " + str(player.name) + " value: " + str(player.evaluate()))
                choice = player.strategy()
                if choice == "hit":
                    player.hit(self.deck)
                    if player.evaluate() > 21:
                        print("Player " + str(player.name) + " cards: " + str(player.cards))
                        print("Player " + str(player.name) + " value: " + str(player.evaluate()))
                        print("Bust!")
                        break
                #dont let players double if they dont have enough chips
                if choice == "double":
                    player.chips -= self.playerBets[index]
                    self.playerBets[index] *= 2
                    player.hit(self.deck)
                    break
                if choice == "stand":
                    break
            
    
    def handleDealer(self):
        self.dealer.cards.append(self.dealer.hiddencard)
        while self.dealer.evaluate() < 17:
            self.dealer.hit(self.deck)
        print("Dealer value:", self.dealer.evaluate())

    def handlePayout(self):
        dealer_value = self.dealer.evaluate()
        if dealer_value > 21:
            #payout everyone not over 21
            player_index = 0
            for player in self.players:
                if player.evaluate() <= 21:
                    player.chips += 2*self.playerBets[player_index]
                player_index += 1
        else:
            player_index = 0
            for player in self.players:
                if player.evaluate() > self.dealer.evaluate() and player.evaluate() <= 21:
                    player.chips += 2*self.playerBets[player_index]
                if player.evaluate() == self.dealer.evaluate():
                    player.chips += self.playerBets[player_index]
                player_index += 1
            


