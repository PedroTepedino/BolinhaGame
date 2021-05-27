from graphics import GraphWin
from graphics import Circle
from vector import Vector
from player import Player


class Ball:

    def __init__(self, pos: Vector, rad: float, vel: float):
        self.position = pos
        self.radius = rad
        self.speed = vel
        self.velocity = Vector(1, 1) * vel
        self.sprite = Circle(self.position.to_point(), self.radius)

    def draw(self, window: GraphWin):
        self.sprite.undraw()
        self.sprite = Circle(self.position.to_point(), self.radius)
        self.sprite.setFill("green")
        self.sprite.draw(window)

    def update(self, window: GraphWin, player: Player):
        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= window.width:
            self.velocity = Vector(-self.velocity.x, self.velocity.y)

        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= window.height:
            self.velocity = Vector(self.velocity.x, -self.velocity.y)

        self.position += self.velocity

        self.collide_player(player)

        self.draw(window)

    def collide_player(self, player: Player):
        height_difference = (self.position.y + self.radius) - (player.position.y - player.half_size.y)
        width_check = self.position.x + self.radius <= player.position.x + player.half_size.x and self.position.x - self.radius >= player.position.x - player.half_size.x

        # Check collision
        if height_difference >= 0 and width_check:
            self.position -= Vector(0, height_difference)
            self.velocity = Vector(self.velocity.x, -self.velocity.y)
