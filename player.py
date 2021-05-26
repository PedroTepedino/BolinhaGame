from graphics import *
import time
win = GraphWin('Bolinha Game', 800, 600)


def player_func(win):
    global current_position
    global velocity
    global player
    player.undraw()
    key = win.checkKey()
    if key == 'Right':
        current_position = Point(current_position.x + velocity, current_position.y)
    elif key == 'Left':
        current_position = Point(current_position.x - velocity, current_position.y)
    player = Rectangle(Point(current_position.x + size.x, current_position.y + size.y),
                       Point(current_position.x - size.x, current_position.y - size.y))
    player.setFill('black')
    player.draw(win)


current_position = Point(400, 500)
size = Point(50, 3)
velocity = 10
player = Rectangle(Point(current_position.x + size.x, current_position.y + size.y),
                   Point(current_position.x - size.x, current_position.y - size.y))
while True:
    player_func(win)
    time.sleep(0.05)


win.close()
