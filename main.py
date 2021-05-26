from graphics import *


win = GraphWin("Bolinha Game", 800, 600)
playing = True

while playing:
    key = win.checkKey()

    if key == "Escape":
        playing = False

win.close()