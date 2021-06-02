from graphics import *


class Score:
    def __init__(self, window: GraphWin):
        self.pts = 0
        self.window = window
        self.pontos = Text(Point(400, 575), f"Pontos: {self.pts}")
        self.pontos.setSize(14)

    def draw(self):
        self.pontos = Text(Point(400, 575), f"Pontos: {self.pts}")
        self.pontos.setSize(14)
        self.pontos.draw(self.window)

    def undraw(self):
        self.pontos.undraw()

    def add_score(self):
        self.pts += 1
        self.pontos.setText(f"Pontos: {self.pts}")

    def reset(self):
        self.pts = 0
        self.undraw()
        self.draw()

# def score(pts, pontos, win):
#     pts += 1
#     pontos.undraw()
#     pontos = Text(Point(400, 575), "Pontos: " + str(pts))
#     pontos.setSize(14)
#     pontos.draw(win)
