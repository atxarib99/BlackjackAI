from Game import Game
from GameWindow import GameWindow
import time

game = Game(numplayers=1)

while True:
    game.window.main.after(500, game.startRound())
#    choice = input("play again? (y/n)")
#    if choice == 'n':
#        break
    time.sleep(1)

# window = GameWindow()
# time.sleep(5)
