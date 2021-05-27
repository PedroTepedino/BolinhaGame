from graphics import *
from ui import *
from ball import Ball
from player import Player
from vector import Vector
import time
from score import *

win = GraphWin("Bolinha Game", 800, 600)

draw_ui(win)
playing = True

ball = Ball(Vector(400, 15), 10, 10)
ball.draw(win)

player = Player(Vector(400,500), Vector(50, 3), 10)
player.draw(win)

pts = 0
pontos=Text(Point(400, 575), "Pontos: " + str(pts))
pontos.setSize(14)
pontos.draw(win)

while playing:
    key = win.checkKey()



    if key == "Escape":
        playing = False
    elif key == "Right":
        player.move_right()
    elif key == 'Left':
        player.move_left()

    player.update(win)
    ball.update(win, player)

    time.sleep(0.05)

win.close()