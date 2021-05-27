from graphics import *
from vector import Vector


class Player:
    def __init__(self, pos: Vector, half_size: Vector, speed: float):
        self.position = pos
        self.half_size = half_size
        self.speed = speed
        self.sprite = Rectangle((pos + half_size).to_point(), (pos - half_size).to_point())
        self.move_velocity = Vector(1, 0) * speed

    def draw(self, window: GraphWin):
        self.sprite.undraw()
        self.sprite = Rectangle((self.position + self.half_size).to_point(), (self.position - self.half_size).to_point())
        self.sprite.setFill('black')
        self.sprite.draw(window)

    def move_right(self):
        self.position += self.move_velocity

    def move_left(self):
        self.position -= self.move_velocity

    def update(self, window: GraphWin):
        if self.position.x + self.half_size.x >= window.width:
            self.position = Vector(window.width - self.half_size.x, self.position.y)
        elif self.position.x - self.half_size.x <= 0:
            self.position = Vector(0 + self.half_size.x, self.position.y)

        self.draw(window)

# win = GraphWin('Bolinha Game', 800, 600)
#
# def player_func(win):
#     global current_position
#     global velocity
#     global player
#     player.undraw()
#     key = win.checkKey()
#     if key == 'Right':
#         current_position = Point(current_position.x + velocity, current_position.y)
#     elif key == 'Left':
#         current_position = Point(current_position.x - velocity, current_position.y)
#     player = Rectangle(Point(current_position.x + size.x, current_position.y + size.y),
#                        Point(current_position.x - size.x, current_position.y - size.y))
#     player.setFill('black')
#     player.draw(win)
#
#
# current_position = Point(400, 500)
# size = Point(50, 3)
# velocity = 10
# player = Rectangle(Point(current_position.x + size.x, current_position.y + size.y),
#                    Point(current_position.x - size.x, current_position.y - size.y))
# while True:
#     player_func(win)
#     time.sleep(0.05)
#
#
# win.close()

