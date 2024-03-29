from Card import Card
from Player import Player

class Human(Player):

    def initagain(self):
        pass

    def createSplit(self, card):
        self.split = Human(self.name+"split1", chip_stack=self.chip_stack)
        self.split.cards.append(card)
    
    #fixed agent always bets minimum
    def askForBets(self):
        bet = -1
        while bet == -1:
            bet = int(input("Player " + str(self.name) + " enter how much you want to bet..."))
            if bet > self.chip_stack.chips:
                bet = -1
                print('bet was too large!')
        return bet

    #fixed agent requires game data
    def setGame(self, game):
        self.game = game

    def strategy(self):
        choice = input("Player " + str(self.name) + " your move [hit,stand,double]...")
        return choice

