import Card
import Player
class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.hiddencard = Card('Heart', 'A')
    