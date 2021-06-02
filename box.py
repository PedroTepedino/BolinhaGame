from vector import Vector


class Box:
    def __init__(self, pos: Vector, half_size: Vector):
        self.position: Vector = pos
        self.half_size = half_size
