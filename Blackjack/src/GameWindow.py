import tkinter as tk
class GameWindow:
    def __init__(self):
        self.main = tk.Tk()
        self.canv = tk.Canvas(self.main, width=1000, height=1000)
        self.canv.pack()
        img = self.getCardImg("Diamond", 10)
        self.canv.create_image(50,50, anchor=tk.NW, image=img)
        self.main.update()
        # filename = PhotoImage(file = "sunshine.gif")
        # image = canvas.create_image(50, 50, anchor = NE, image = filename)

    def getCardImg(self, suit, char):
        suitChar = suit[0]
        cardImgName = "/Users/aribdhuka/PythonProjects/BlackjackAI/Blackjack/res/cards/" + str(char) + suitChar + ".png"
        print(cardImgName)
        return tk.PhotoImage(file=cardImgName) #691,1056
