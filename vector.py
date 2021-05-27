import math
from graphics import Point


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __truediv__(self, other: float):
        return Vector(self.x / other, self.y / other)

    def dot(self, other) -> float:
        return (self.x * other.x) + (self.y * other.y)

    def cos_angle(self, other) -> float:
        return self.dot(other) / (self.mag() * other.mag())

    def normalized(self):
        return self / self.mag()

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other)

    def mag2(self):
        return (self.x * self.x) + (self.y * self.y)

    def mag(self):
        return math.sqrt(self.mag2())

    def to_point(self) -> Point:
        return Point(self.x, self.y)
