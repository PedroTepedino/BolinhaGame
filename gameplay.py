from ball import Ball
from button import Button
from player import Player
from scene import Scene
from graphics import *

from score import Score
from vector import Vector


class Gameplay(Scene):

    def __init__(self, window: GraphWin, unpause_function, back_to_menu_function, exit_function):
        self.window = window

        self.paused = False
        self.pause_ui = PauseUi(self.window, unpause_function, back_to_menu_function,  exit_function)

        self.score = Score(self.window)
        self.ball = Ball(Vector(400, 15), 10, 10, Vector(1, 1).normalized(), self.score)
        self.player = Player(Vector(400, 500), Vector(50, 3), 10)

        self.linha_esquerda = Line(Point(0, 50), Point(0, 550))
        self.linha_direita = Line(Point(800, 50), Point(800, 550))
        self.linha_inferior = Line(Point(0, 575), Point(800, 575))
        self.linha_superior = Line(Point(0, 25), Point(800, 25))

        self.diabins = [Image(Point(200, 555), 'diabin.PNG'), Image(Point(600, 560), 'diabin.PNG')]
        self.clouds = []
        self.fogos = []

        self.linha_superior.setWidth(50)
        self.linha_superior.setFill(color_rgb(50, 50, 180))

        self.linha_inferior.setWidth(50)
        self.linha_inferior.setFill(color_rgb(250, 80, 80))

        self.linha_direita.setWidth(25)
        self.linha_direita.setFill(color_rgb(50, 50, 50))

        self.linha_esquerda.setWidth(25)
        self.linha_esquerda.setFill(color_rgb(50, 50, 50))

        for i in range(3):
            self.fogos.append(Image(Point(150 + (300 * i), 575), 'fogo.PNG'))

        for i in range(4):
            self.clouds.append(Image(Point(110 + (200 * i), 25), 'cloud.JPG'))

        self.window.setBackground('gray')

    def draw(self):
        self.ball.reset()

        self.linha_superior.draw(self.window)
        self.linha_inferior.draw(self.window)
        self.linha_direita.draw(self.window)
        self.linha_esquerda.draw(self.window)

        for i in range(3):
            self.fogos[i].draw(self.window)

        for i in range(4):
            self.clouds[i].draw(self.window)

        for i in range(len(self.diabins)):
            self.diabins[i].draw(self.window)

        self.player.draw(self.window)
        self.ball.draw(self.window)
        self.score.draw()

    def undraw(self):
        self.paused = False

        self.player.undraw()
        self.ball.undraw()
        self.score.undraw()
        self.pause_ui.hide()

        self.linha_superior.undraw()
        self.linha_inferior.undraw()
        self.linha_direita.undraw()
        self.linha_esquerda.undraw()

        for i in range(3):
            self.fogos[i].undraw()

        for i in range(4):
            self.clouds[i].undraw()

        for i in range(len(self.diabins)):
            self.diabins[i].undraw()

    def tick(self, mouse_position: Vector, mouse_click_position):
        if not self.paused:
            self.player.update(self.window)
            self.ball.update(self.window, self.player)
        else:
            self.pause_ui.update(mouse_position, mouse_click_position)

    def move_player(self, direction: str):
        if self.paused:
            return

        if direction == "right":
            self.player.move_right()
        elif direction == "left":
            self.player.move_left()

    def pause(self):
        self.paused = not self.paused

        if self.paused:
            self.pause_ui.show()
        else:
            self.pause_ui.hide()


class PauseUi:
    def __init__(self, window: GraphWin, unpause_function, back_to_menu_function, exit_function):
        self.window = window

        self.panel = Rectangle(Point(200, 100), Point(600, 500))
        self.panel.setFill(color_rgb(190, 190, 190))
        self.panel.setOutline("black")
        self.panel.setWidth(10)

        self.resume_button = Button(window, unpause_function, Vector(400, 275), Vector(75, 25), "Resume")
        self.menu_button = Button(window, back_to_menu_function, Vector(400, 350), Vector(70, 20), "Menu")
        self.exit_button = Button(window, exit_function, Vector(400, 425), Vector(70, 20), "Exit")

        self.title = Text(Point(405, 150), "Pause!")
        self.title.setSize(30)

    def show(self):
        self.panel.draw(self.window)
        self.resume_button.draw()
        self.menu_button.draw()
        self.exit_button.draw()
        self.title.draw(self.window)

    def hide(self):
        self.panel.undraw()
        self.resume_button.undraw()
        self.menu_button.undraw()
        self.exit_button.undraw()
        self.title.undraw()

    def update(self, mouse_position: Vector, mouse_click_position):
        self.resume_button.tick(mouse_position, mouse_click_position)
        self.menu_button.tick(mouse_position, mouse_click_position)
        self.exit_button.tick(mouse_position, mouse_click_position)
