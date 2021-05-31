import random
from graphics import *
from menu import Menu
from gameplay import Gameplay
from ui import *
from ball import Ball
from player import Player
from vector import Vector
import time
from score import Score
from enum import Enum


# draw_ui(win)
#
# score = Score(win)

# ball = Ball(Vector(400, 15), 10, 10, Vector(1, 1).normalized(), score)
# ball.draw(win)
#
# player = Player(Vector(400, 500), Vector(50, 3), 10)
# player.draw(win)

# pts = 0
# pontos=Text(Point(400, 575), "Pontos: " + str(pts))
# pontos.setSize(14)
# pontos.draw(win)

current_mouse_position = Vector(0, 0)


def motion(event):
    global current_mouse_position
    x, y = event.x, event.y
    current_mouse_position = Vector(x, y)


class BolinhaGame:
    def __init__(self):
        self.current_mouse_position = Vector(0, 0)
        self.playing = True
        self.frame_rate = 0.05

        self.win = GraphWin("Bolinha Game", 800, 600)
        self.win.bind('<Motion>', motion)

        self.menu_scene = Menu(self.win, self.begin_gameplay, self.credits_switch, self.exit_game)
        self.gameplay_scene = Gameplay()

        self.menu_scene.draw()

        self.current_scene = self.menu_scene

    def main(self):
        while self.playing:
            if self.win.isClosed():
                break

            key = self.win.checkKey()
            mouse_click = self.win.checkMouse()

            self.menu_scene.mouse_click = mouse_click
            self.menu_scene.mouse_position = current_mouse_position

            if key == "Escape":
                if type(self.current_scene) is Menu:
                    self.playing = False
                elif type(self.current_scene) is Gameplay:
                    self.change_scene("menu")
            # elif key == "Right":
            #     player.move_right()
            # elif key == 'Left':
            #     player.move_left()
            #
            # player.update(win)
            # ball.update(win, player)

            self.current_scene.tick()

            time.sleep(self.frame_rate)
        self.win.close()

    def begin_gameplay(self):
        self.change_scene("play")

    def credits_switch(self):
        pass

    def exit_game(self):
        self.playing = False

    def change_scene(self, next_scene: str):
        self.current_scene.undraw()

        if next_scene == "play":
            self.current_scene = self.gameplay_scene
        elif next_scene == "menu":
            self.current_scene = self.menu_scene

        self.current_scene.draw()


if __name__ == "__main__":
    BolinhaGame().main()
