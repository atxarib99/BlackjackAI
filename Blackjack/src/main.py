from Game import Game
from GameWindow import GameWindow
import time
game = Game(numplayers=1)

while True:
    game.startRound()
    choice = input("play again? (y/n)")
    if choice == 'n':
        break

# window = GameWindow()
# time.sleep(5)
