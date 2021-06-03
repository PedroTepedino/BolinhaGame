from graphics import *
from vector import Vector
from box import Box


class Player(Box):
    def __init__(self, pos: Vector, half_size: Vector, speed: float):
        super().__init__(pos, half_size)
        self.initial_speed = speed
        self.initial_position = pos
        self.sprite = Rectangle((pos + half_size).to_point(), (pos - half_size).to_point())
        self.move_velocity = Vector(1, 0) * speed
        self.new_position = pos
        self.current_speed = speed

    def draw(self, window: GraphWin):
        self.sprite.undraw()
        self.sprite = Rectangle((self.position + self.half_size).to_point(), (self.position - self.half_size).to_point())
        self.sprite.setFill('black')
        self.sprite.draw(window)

    def undraw(self):
        self.sprite.undraw()

    def move_right(self):
        self.new_position = self.position + self.move_velocity

    def move_left(self):
        self.new_position = self.position - self.move_velocity

    def update(self, window: GraphWin):
        self.move_velocity = self.move_velocity.normalized() * self.current_speed

        if self.new_position.x + self.half_size.x >= window.width:
            self.new_position = Vector(window.width - self.half_size.x, self.position.y)
        elif self.new_position.x - self.half_size.x <= 0:
            self.new_position = Vector(0 + self.half_size.x, self.position.y)

        delta_position = self.new_position - self.position
        self.sprite.move(delta_position.x, delta_position.y)

        self.position = self.new_position

        # self.draw(window)

    def reset(self):
        self.current_speed = self.initial_speed
        self.new_position = self.initial_position

        delta = self.new_position - self.position
        self.sprite.move(delta.x, delta.y)
        self.position = self.new_position

    def change_speed(self, new_speed):
        self.current_speed = self.initial_speed + new_speed

