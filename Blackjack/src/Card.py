def Card:
    def __init__(self, suit, char):
        self.suit = suit
        self.char = char
    
    def evaluate(self):
        #todo Dynamic aces
        if self.char = 'A':
            return 11
        if self.char = 'K' or self.char = 'Q' or self.char = 'J':
            return 10
        else:
            return int(self.char)
