from graphics import GraphWin
from graphics import Circle
from vector import Vector
from player import Player
from score import Score


class Ball:

    def __init__(self, window: GraphWin, initial_position: Vector, radius: float, speed: float, initial_direction: Vector, score: Score, lose_life_function):
        self.window = window

        self.initial_direction = initial_direction
        self.initial_position = initial_position
        self.radius = radius
        self.speed = speed
        self.score = score

        self.is_alive = True
        self.still_ball = True

        self.position = self.initial_position
        self.velocity = self.initial_direction * speed

        self.sprite = Circle(self.position.to_point(), self.radius)

        self.damage = lose_life_function

    def draw(self, window: GraphWin):
        self.sprite.undraw()
        self.sprite = Circle(self.position.to_point(), self.radius)
        self.sprite.setFill("green")
        self.sprite.draw(window)

    def undraw(self):
        self.sprite.undraw()

    def reset(self):
        self.move_ball(self.initial_position)
        self.velocity = self.initial_direction * self.speed
        self.is_alive = True
        self.still_ball = True

    def release(self):
        self.still_ball = False

    def kill_ball(self):
        pass

    def update(self,  player: Player):
        if self.still_ball:
            self.move_ball(player.position + Vector(0, -(self.radius + 10)))
            return

        self.world_collide()
        self.move_ball(self.collide_player(player))

    def move_ball(self, new_position: Vector):
        delta = new_position - self.position
        self.sprite.move(delta.x, delta.y)
        self.position = new_position

    def world_collide(self):
        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= self.window.width:
            self.velocity = Vector(-self.velocity.x, self.velocity.y)

        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= self.window.height:
            self.velocity = Vector(self.velocity.x, -self.velocity.y)

            if self.position.y > self.window.height / 2:
                self.damage()

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

            self.score.add_score()

        return potential_position
