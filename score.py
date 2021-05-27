from graphics import *
def score(pts, pontos, win):
    pts += 1
    pontos.undraw()
    pontos=Text(Point(400, 575), "Pontos: " + str(pts))
    pontos.setSize(14)
    pontos.draw(win)