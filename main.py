from graphics import *
from ui import *
from score import *

win = GraphWin("Bolinha Game", 800, 600)

draw_ui(win)
playing = True


pts = 0
pontos=Text(Point(400, 575), "Pontos: " + str(pts))
pontos.setSize(14)
pontos.draw(win)


while playing:
    key = win.checkKey()

    if key == "Escape":
        playing = False

win.close()