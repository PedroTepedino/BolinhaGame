from graphics import *

from vector import Vector


class Score:
    def __init__(self, window: GraphWin):
        self.pts = 0
        self.window = window
        position = Vector(400, 575)
        half_size = Vector(75, 20)
        self.pontos = Text(Point(400, 575), f"Pontos: {self.pts}")
        self.pontos.setSize(14)

        self.background = Rectangle((position + half_size).to_point(), (position - half_size).to_point())
        self.background.setFill(color_rgb(230, 230, 230))
        self.background.setOutline("black")

    def draw(self):
        self.background.draw(self.window)
        self.pontos.setText(f"Pontos: {self.pts}")
        self.pontos.draw(self.window)

    def undraw(self):
        self.background.undraw()
        self.pontos.undraw()

    def add_score(self):
        self.pts += 1
        self.pontos.setText(f"Pontos: {self.pts}")

    def reset(self):
        self.pts = 0
        self.pontos.setText(f"Pontos: {self.pts}")

# def score(pts, pontos, win):
#     pts += 1
#     pontos.undraw()
#     pontos = Text(Point(400, 575), "Pontos: " + str(pts))
#     pontos.setSize(14)
#     pontos.draw(win)
