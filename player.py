from graphics import *
from vector import Vector


class Player:
    def __init__(self, pos: Vector, half_size: Vector, speed: float):
        self.position = pos
        self.half_size = half_size
        self.speed = speed
        self.sprite = Rectangle((pos + half_size).to_point(), (pos - half_size).to_point())
        self.move_velocity = Vector(1, 0) * speed
        self.new_position = pos

    def draw(self, window: GraphWin):
        self.sprite.undraw()
        self.sprite = Rectangle((self.position + self.half_size).to_point(), (self.position - self.half_size).to_point())
        self.sprite.setFill('black')
        self.sprite.draw(window)

    def move_right(self):
        self.new_position = self.position + self.move_velocity

    def move_left(self):
        self.new_position = self.position - self.move_velocity

    def update(self, window: GraphWin):
        if self.new_position.x + self.half_size.x >= window.width:
            self.new_position = Vector(window.width - self.half_size.x, self.position.y)
        elif self.new_position.x - self.half_size.x <= 0:
            self.new_position = Vector(0 + self.half_size.x, self.position.y)

        delta_position = self.new_position - self.position
        self.sprite.move(delta_position.x, delta_position.y)

        self.position = self.new_position

        # self.draw(window)
