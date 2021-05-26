from graphics import *
from ui import *

win = GraphWin("Bolinha Game", 800, 600)

draw_ui(win)
playing = True

while playing:
    key = win.checkKey()

    if key == "Escape":
        playing = False

win.close()