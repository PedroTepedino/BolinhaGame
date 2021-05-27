from graphics import *
from ui import *
from ball import Ball
from vector import Vector
import time

win = GraphWin("Bolinha Game", 800, 600)
playing = True

ball = Ball(Vector(400, 15), 10, 10)
ball.draw(win)

while playing:
    key = win.checkKey()

    ball.update(win)

    if key == "Escape":
        playing = False

    time.sleep(0.05)

win.close()