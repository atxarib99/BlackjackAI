from Card import Card
from Player import Player

class FixedAgent(Player):

    def initagain(self):
        self.table = None
        self.table = self.loadLookupTable()

    def loadLookupTable(self):

        def strip(inp):
            return inp.replace('\n','').replace(' ','').replace('\t','')

        tableFile = open("table.tb", "r")
        lines = tableFile.readlines()
        table = {}
        dealerVals = lines[0].split('\t')
        dealerVals.pop(0)
        for elem in dealerVals:
            table[strip(elem)] = {}

        def convert(old):
            #implement split later :(
            if old == 'SP':
                return 'split'

            if old[0] == 'S':
                return 'stand'
            if old[0] == 'H':
                return 'hit'
            if old[0] == 'D':
                return 'double'
            if old[0] == 'U':
                if old[1] == 's':
                    return 'stand'
                if old[1] == 'h':
                    return 'hit'
                if old[1] == 'd':
                    return 'double'

        lines.pop(0)
        for line in lines:
            strats = line.split('\t')
            playerVal = strip(strats.pop(0))
            for dv,index in zip(list(table.keys()), range(0,len(list(table.keys())))):
                table[dv][playerVal] = convert(strip(strats[index]))

        return table


    def createSplit(self, card):
        self.split = FixedAgent(self.name+"split1", chip_stack=self.chip_stack)
        self.split.setGame(self.game)
        self.split.cards.append(card)
       

    #fixed agent always bets minimum
    def askForBets(self):
        return 10

    #fixed agent requires game data
    def setGame(self, game):
        self.game = game

    def strategy(self):
        showcard = self.game.dealer.evaluate()
        if showcard == 11:
            showcard = 'A'
        myval = self.evaluate()
        #ERROR: This handling is incorrect! after player.hit() this fails!
        #handle soft
        if self.cards[0].char == 'A' or self.cards[1].char == 'A':
            #if we have exactly two cards
            if len(self.cards) == 2:
                if self.cards[0].char == 'A':
                    myval = 'A' + str(self.cards[1].char)
                if self.cards[1].char == 'A':
                    myval = 'A' + str(self.cards[0].char)
            else:
                #TODO: figure out if we are soft, and set to equiv table entry. For now image everything is hard.
                #its almost right, we will mess us stuff like soft 16.
                pass
        #handle pairs if we have exactly two cards
        if self.cards[0].char == self.cards[1].char and len(self.cards) == 2:
            if self.cards[0].evaluate() == 10:
                myval = 'TT'
            else:
                myval = str(self.cards[0].char) + str(self.cards[1].char)
        strat = self.table[str(showcard)][str(myval)]
        #can we get stuck in a 'hit -> double' loop?
        print(strat)
        return strat



        

