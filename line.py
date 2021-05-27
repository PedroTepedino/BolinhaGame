from vector import Vector


class Line:
    def __init__(self, v1: Vector, v2: Vector):
        self.p1 = v1
        self.p2 = v2
        self.m = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        self.a = self.m
        self.b = -(self.m * self.p1.x) - self.p1.y

    def intersection_point(self: Line, other: Line) -> Vector:
        if self.m == other.m:
            return Vector(-1, -1)

        x = (other.b - self.b) / (self.a - other.a)
        y = (self.a * x) + other.b


