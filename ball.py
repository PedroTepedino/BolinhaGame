from typing import Sequence

from graphics import GraphWin
from graphics import Circle

from box import Box
from pointsquare import PointSquare
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

    def update(self, player: Player, squares: Sequence[PointSquare]):
        if self.still_ball:
            self.move_ball(player.position + Vector(0, -(self.radius + 10)))
            return

        self.world_collide()

        potential_position = self.position + self.velocity

        new_potential_position, collided = self.collide_player(player)

        if collided:
            potential_position = new_potential_position
        else:
            for square in squares:
                if not square.is_active:
                    continue

                new_potential_position, collided = self.collide_player(square)
                if collided:
                    square.hit()
                    potential_position = new_potential_position
                    break

        self.move_ball(potential_position)

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

    def collide_player(self, box_collider: Box):

        potential_position = self.position + self.velocity
        collided = False

        if type(box_collider) is Player:
            is_player = True
        else :
            is_player = False

        nearest_point = Vector(0, 0)
        nearest_point.x = max(box_collider.position.x - box_collider.half_size.x,
                              min(potential_position.x, box_collider.position.x + box_collider.half_size.x))
        nearest_point.y = max(box_collider.position.y - box_collider.half_size.y,
                              min(potential_position.y, box_collider.position.y + box_collider.half_size.y))

        ray_to_nearest = nearest_point - potential_position
        overlap = self.radius - ray_to_nearest.mag()

        if ray_to_nearest.mag() == 0:
            overlap = 0

        if overlap > 0:
            potential_position = potential_position - (ray_to_nearest.normalized() * overlap)

            right = (Vector(1, 0)).cos_angle(potential_position - box_collider.position)
            right_rec = (Vector(1, 0)).cos_angle(Vector(box_collider.half_size.x, -box_collider.half_size.y))
            left_rec = (Vector(1, 0)).cos_angle(Vector(-box_collider.half_size.x, -box_collider.half_size.y))

            collided_top = left_rec <= right <= right_rec

            top = (Vector(0, 1)).cos_angle(potential_position - box_collider.position)
            down_rec = (Vector(0, 1)).cos_angle(Vector(-box_collider.half_size.x, box_collider.half_size.y))
            top_rec = (Vector(0, 1)).cos_angle(Vector(-box_collider.half_size.x, -box_collider.half_size.y))

            collided_right = top_rec <= top <= down_rec

            if collided_top:
                if not is_player:
                    self.velocity = Vector(self.velocity.x, -self.velocity.y)
                else:
                    self.velocity = (potential_position - box_collider.position).normalized() * self.speed
                # self.speed += 10
                # self.velocity = self.velocity.normalized() * self.speed

            elif collided_right:
                self.velocity = Vector(-self.velocity.x, self.velocity.y)
                # self.speed += 10
                # self.velocity = self.velocity.normalized() * self.speed

            if not is_player:
                self.score.add_score()

            collided = True

        return potential_position, collided
