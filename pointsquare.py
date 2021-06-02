from box import Box
from vector import Vector
from graphics import *


class PointSquare(Box):
    def __init__(self, window: GraphWin,  pos: Vector, half_size: Vector, color):
        super().__init__(pos, half_size)

        self.window = window

        self.is_active = True

        self.sprite = Rectangle((self.position + self.half_size).to_point(), (self.position - self.half_size).to_point())
        self.sprite.setFill(color)

    def show(self):
        self.sprite.draw(self.window)

    def hide(self):
        self.sprite.undraw()

    def hit(self):
        self.is_active = False
        self.hide()

    def reset(self):
        self.is_active = True