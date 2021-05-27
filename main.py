from graphics import *
from ui import *
from ball import Ball
from vector import Vector
import time
from score import *

win = GraphWin("Bolinha Game", 800, 600)

draw_ui(win)
playing = True

ball = Ball(Vector(400, 15), 10, 10)
ball.draw(win)

pts = 0
pontos=Text(Point(400, 575), "Pontos: " + str(pts))
pontos.setSize(14)
pontos.draw(win)


while playing:
    key = win.checkKey()

    ball.update(win)

    if key == "Escape":
        playing = False

    time.sleep(0.05)

win.close()