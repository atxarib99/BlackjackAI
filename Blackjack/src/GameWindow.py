import tkinter as tk
from PIL import Image,ImageTk
import time

width, height = 1000,1000
cardWidth, cardHeight = 138,211

class GameWindow:
    def __init__(self):
        self.images = []
        self.main = tk.Tk()
        self.canv = tk.Canvas(self.main, width=width, height=height)
        self.canv.pack()
        img = self.getCardImg("Diamond", 10)
        self.canv.create_image(50,50, anchor=tk.NW, image=img)
        self.main.update()
        # filename = PhotoImage(file = "sunshine.gif")
        # image = canvas.create_image(50, 50, anchor = NE, image = filename)

    def getCardImg(self, suit, char):
        suitChar = suit[0]
        cardImgName = "/home/aribd/Documents/PythonProjects/BlackjackAI/Blackjack/res/cards/" + str(char) + suitChar + ".png"
        cardImg = Image.open(cardImgName)
        cardImg = cardImg.resize((cardWidth, cardHeight), Image.ANTIALIAS)
        return ImageTk.PhotoImage(cardImg) #orig size 691,1056
    
    def getCardBack(self):
        cardImgName = "/home/aribd/Documents/PythonProjects/BlackjackAI/Blackjack/res/cards/red_back.png"
        cardImg = Image.open(cardImgName)
        cardImg = cardImg.resize((cardWidth, cardHeight), Image.ANTIALIAS)
        return ImageTk.PhotoImage(cardImg) #orig size 691,1056

    def drawGameState(self, gameState, drawBlank=True):
        self.canv.delete('all')
        self.images.clear()
        #draw dealer at middle top
        x = width / 2 - (cardWidth/2) #middle minus half card width
        y = 10 #margin
        for card in gameState.dealer.cards:
            self.images.append(self.getCardImg(card.suit,card.char))
            self.canv.create_image(x,y,anchor=tk.NW, image=self.images[-1])
            x+=50
        #draw blank
        if drawBlank:
            self.images.append(self.getCardBack())
            self.canv.create_image(x,y,anchor=tk.NW, image=self.images[-1])

        #lets just do one player first for my sanity middle bottom

        #max 3 players again for my sanity :)
        
        for player in gameState.players:

            x=0
            y=0
            if player.name == '0':
                x = width - cardWidth - (((len(player.cards)) - 1) * 50)
                y = height/2

            if player.name == '1':
                x = width / 2 - (cardWidth/2)
                y = height - 10

            if player.name == '2':
                x = 10
                y = height/2
                
            for card in player.cards:
                self.images.append(self.getCardImg(card.suit,card.char))
                self.canv.create_image(x,y,anchor=tk.SW, image=self.images[-1])
                x+=50

        self.canv.pack()
        self.main.update()


