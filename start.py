from core.game import Game

game = Game(100, True)
key = False

while not key:
    key = game.play()
