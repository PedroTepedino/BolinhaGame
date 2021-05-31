from graphics import GraphWin
from graphics import Circle
from vector import Vector
from player import Player
from score import Score


class Ball:

    def __init__(self, initial_position: Vector, radius: float, speed: float, initial_direction: Vector, score: Score):
        self.position = initial_position
        self.radius = radius
        self.speed = speed
        self.velocity = initial_direction * speed
        self.sprite = Circle(self.position.to_point(), self.radius)
        self.score = score

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

        new_position = self.collide_player(player)

        self.sprite.move(new_position.x - self.position.x, new_position.y - self.position.y)

        self.position = new_position

        # self.draw(window)

    def collide_player(self, player: Player):

        potential_position = self.position + self.velocity

        nearest_point = Vector(0, 0)
        nearest_point.x = max(player.position.x - player.half_size.x,
                              min(potential_position.x, player.position.x + player.half_size.x))
        nearest_point.y = max(player.position.y - player.half_size.y,
                              min(potential_position.y, player.position.y + player.half_size.y))

        ray_to_nearest = nearest_point - potential_position
        overlap = self.radius - ray_to_nearest.mag()

        if ray_to_nearest.mag() == 0:
            overlap = 0

        if overlap >= 0:
            potential_position = potential_position - (ray_to_nearest.normalized() * overlap)

            right = (Vector(1, 0)).cos_angle(potential_position - player.position)
            right_rec = (Vector(1, 0)).cos_angle(Vector(player.half_size.x, -player.half_size.y))
            left_rec = (Vector(1, 0)).cos_angle(Vector(-player.half_size.x, -player.half_size.y))

            collided_top = left_rec <= right <= right_rec

            top = (Vector(0, 1)).cos_angle(potential_position - player.position)
            down_rec = (Vector(0, 1)).cos_angle(Vector(-player.half_size.x, player.half_size.y))
            top_rec = (Vector(0, 1)).cos_angle(Vector(-player.half_size.x, -player.half_size.y))

            collided_right = top_rec <= top <= down_rec

            if collided_top:
                self.velocity = Vector(self.velocity.x, -self.velocity.y)
                # self.speed += 10
                # self.velocity = self.velocity.normalized() * self.speed

            if collided_right:
                self.velocity = Vector(-self.velocity.x, self.velocity.y)
                # self.speed += 10
                # self.velocity = self.velocity.normalized() * self.speed

        return potential_position
