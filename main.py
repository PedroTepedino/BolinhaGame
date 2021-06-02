from highscore import HighScore
import random
from graphics import *
from menu import Menu
from gameplay import Gameplay
from ui import *
from vector import Vector
import time
from highscore import HighScore

current_mouse_position = Vector(0, 0)


def motion(event):
    global current_mouse_position
    current_mouse_position = Vector(event.x, event.y)


class BolinhaGame:
    def __init__(self):
        self.current_mouse_position = Vector(0, 0)
        self.playing = True
        self.frame_rate = 0.05

        self.win = GraphWin("Bolinha Game", 800, 600)
        self.win.bind('<Motion>', motion)

        self.highscore = HighScore()

        self.menu_scene = Menu(self.win, self.begin_gameplay, self.credits_switch, self.exit_game, self.credits_switch)
        self.gameplay_scene = Gameplay(self.win, self.pause, self.back_to_menu, self.exit_game, self.restart, self.highscore)

        self.menu_scene.draw()

        self.current_scene = self.menu_scene

    def main(self):
        while self.playing:
            if self.win.isClosed():
                break

            key = self.win.checkKey()
            mouse_click = self.win.checkMouse()

            mouse_position = current_mouse_position

            if type(self.current_scene) is Menu:
                if key == "Escape":
                    self.playing = False
            elif type(self.current_scene) is Gameplay:
                if key == "Escape":
                    if not self.gameplay_scene.lost:
                        self.pause()
                elif key == "Right":
                    self.gameplay_scene.move_player("right")
                elif key == 'Left':
                    self.gameplay_scene.move_player("left")
                elif key == 'space':
                    self.gameplay_scene.start_game()

            self.current_scene.tick(mouse_position, mouse_click)
            time.sleep(self.frame_rate)
        self.win.close()

    def begin_gameplay(self):
        self.change_scene("play")

    def credits_switch(self):
        self.menu_scene.credits()

    def exit_game(self):
        self.playing = False

    def back_to_menu(self):
        self.change_scene("menu")

    def pause(self):
        self.gameplay_scene.pause()

    def restart(self):
        print("restart")

    def change_scene(self, next_scene: str):
        self.current_scene.undraw()

        if next_scene == "play":
            self.current_scene = self.gameplay_scene
        elif next_scene == "menu":
            self.current_scene = self.menu_scene

        self.current_scene.draw()


if __name__ == "__main__":
    BolinhaGame().main()
