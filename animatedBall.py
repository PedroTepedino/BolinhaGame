import random

from graphics import *
from vector import Vector


class AnimaBola:

    def __init__(self,
                 window: GraphWin,
                 initial_position: Vector,
                 radius: float = 10,
                 initial_direction: Vector = Vector(1, 1),
                 speed: float = 10,
                 initial_color=color_rgb(18, 10, 143),
                 is_color_random: bool = False,
                 color_range: list = None):
        self.radius = radius
        self.window = window
        self.position = initial_position
        self.speed = speed
        if initial_direction.mag() <= 0.2:
            initial_direction = Vector(1, -1)
        self.velocity = initial_direction.normalized() * speed
        self.random_color = is_color_random
        self.color_range = color_range

        if self.random_color:
            self.color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self.color = initial_color

        self.bola = Circle(self.position.to_point(), self.radius)
        self.bola.setFill(self.color)

    def draw(self):
        self.bola.draw(self.window)

    def undraw(self):
        self.bola.undraw()

    def update(self):
        collided = False

        if self.position.x + self.radius >= 800 or self.position.x - self.radius <= 0:
            collided = True
            self.velocity.x *= -1
            self.velocity.y *= random.randrange(-10, 10)
            self.velocity = self.velocity.normalized() * self.speed
            if self.position.x > self.window.width / 2:
                self.position.x = self.window.width - (self.radius + 1)
            else:
                self.position.x = 0 + self.radius + 1

        if self.position.y + self.radius > self.window.height or self.position.y - self.radius < 0:
            collided = True
            self.velocity.y *= -1
            self.velocity.x *= random.randrange(-10, 10)
            self.velocity = self.velocity.normalized() * self.speed
            if self.position.y > self.window.height / 2:
                self.position.y = self.window.height - self.radius
            else:
                self.position.y = 0 + self.radius

        self.bola.move(self.velocity.x, self.velocity.y)

        self.position += self.velocity

        if collided and self.random_color:
            self.bola.setFill(self.get_random_color())

    def get_random_color(self):
        if self.color_range is not None and len(self.color_range) > 0:
            return self.color_range[random.randint(0, len(self.color_range))]
        else:
            return color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
