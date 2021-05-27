from graphics import *


class Score:
    def __init__(self, window: GraphWin):
        self.pts = 0
        self.window = window
        self.pontos = Text(Point(400, 575), "Pontos: " + str(self.pts))
        self.pontos.setSize(14)
        self.pontos.draw(self.window)

    def draw(self):
        self.pontos.undraw()
        self.pontos = Text(Point(400, 575), "Pontos: " + str(self.pts))
        self.pontos.setSize(14)
        self.pontos.draw(self.window)

    def add_score(self):
        self.pts += 1
        self.draw()

# def score(pts, pontos, win):
#     pts += 1
#     pontos.undraw()
#     pontos = Text(Point(400, 575), "Pontos: " + str(pts))
#     pontos.setSize(14)
#     pontos.draw(win)
