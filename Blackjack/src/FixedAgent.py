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
                return 'stand'

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

        print(table)
        return table


       

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
        #handle soft
        if self.cards[0].char == 'A' or self.cards[1].char == 'A':
            if self.cards[0].char == 'A':
                myval = 'A' + str(self.cards[1].char)
            if self.cards[1].char == 'A':
                myval = 'A' + str(self.cards[0].char)
        #handle pairs
        if self.cards[0].char == self.cards[1].char:
            if self.cards[0].evaluate() == 10:
                myval = 'TT'
            else:
                myval = str(self.cards[0].char) + str(self.cards[1].char)
        strat = self.table[str(showcard)][str(myval)]
        print(showcard)
        print(myval)
        print(strat)
        return strat



        

