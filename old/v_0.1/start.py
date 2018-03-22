from core.game import Game

game = Game(10, True)
key = False

while not key:
    key = game.play()
