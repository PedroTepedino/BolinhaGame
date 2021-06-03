from graphics import *
import random

from scene import Scene
from button import Button
from vector import Vector
from animatedBall import AnimaBola
from abstractui import AbstractUi

"""
O menu será inserido em uma janela de 800x600, possuindo assim, 
3 retangulos do meio pra baixo (play, credits, exit), um texto centralizado em cima, "Bolinha Game",
e uma bolinha no fundo indo e voltando batendo nas paredes.
"""


class Menu(Scene):

    def __init__(self, window: GraphWin, play_func, credits_func, exit_func, credits_function):
        self.win = window

        self.title = Text(Point(405, 150), "Little Ball Game!")
        self.title.setSize(30)

        self.credits_ui = CreditsUi(window, credits_function)

        self.play_button = Button(window, play_func, Vector(400, 275), Vector(75, 25), "Play")
        self.credits_button = Button(window, credits_func, Vector(400, 350), Vector(75, 25), "Credits")
        self.exit_button = Button(window, exit_func, Vector(400, 425), Vector(75, 25), "Exit")

        self.bolas = []

        for _ in range(50):
            self.bola = AnimaBola(window,
                                  initial_position=Vector(random.randint(50, 750), random.randint(50, 550)),
                                  initial_direction=Vector(random.randrange(-10, 10), random.randrange(-10, 10)),
                                  is_color_random=True
                                  )
            self.bolas.append(self.bola)

        self.win.setBackground('gray')

    def draw(self):
        for bola in self.bolas:
            bola.draw()
        self.title.draw(self.win)
        self.play_button.draw()
        self.credits_button.draw()
        self.exit_button.draw()

    def undraw(self):
        for bola in self.bolas:
            bola.undraw()
        self.title.undraw()
        self.play_button.undraw()
        self.credits_button.undraw()
        self.exit_button.undraw()
        self.credits_ui.hide()

    def tick(self, mouse_position: Vector, mouse_click_position):
        if not self.credits_ui.is_open:
            self.play_button.tick(mouse_position, mouse_click_position)
            self.credits_button.tick(mouse_position, mouse_click_position)
            self.exit_button.tick(mouse_position, mouse_click_position)
        else:
            self.credits_ui.update(mouse_position, mouse_click_position)

        for bola in self.bolas:
            bola.update()

    def credits(self):
        if self.credits_ui.is_open:
            self.credits_ui.hide()
        else:
            self.credits_ui.show()


class CreditsUi(AbstractUi):
    def __init__(self, window: GraphWin, exit_credits_function):
        self.window = window

        self.is_open = False

        self.panel = Rectangle(Point(200, 100), Point(600, 500))
        self.panel.setFill(color_rgb(190, 190, 190))
        self.panel.setOutline("black")
        self.panel.setWidth(10)

        self.title = Text(Point(405, 150), "Credits")
        self.title.setSize(30)

        self.tepe_text = Text(Point(405, 200), "Pedro Tepedino: 22105631")
        self.tepe_text.setSize(20)

        self.leo_bom_text = Text(Point(405, 230), "Leonardo Benttes: 22103833")
        self.leo_bom_text.setSize(20)

        self.mc_pose_text = Text(Point(405, 260), "Alexandre Beck: 22104778")
        self.mc_pose_text.setSize(20)

        self.sands_text = Text(Point(405, 290), "Leonardo Areias: 22101570")
        self.sands_text.setSize(20)

        self.zosin_text = Text(Point(405, 320), "Lucas Zoser: 22105593")
        self.zosin_text.setSize(20)

        self.vinil_text = Text(Point(405, 350), "Luiz Paulo França: 22106861")
        self.vinil_text.setSize(20)

        self.ricardao_text = Text(Point(405, 380), "Ricardo Pascotini: 22105830")
        self.ricardao_text.setSize(20)

        self.exit_button = Button(self.window, exit_credits_function, Vector(400, 450), Vector(75, 25), "Back")

    def show(self):
        self.is_open = True

        self.panel.draw(self.window)
        self.title.draw(self.window)

        self.tepe_text.draw(self.window)
        self.leo_bom_text.draw(self.window)
        self.mc_pose_text.draw(self.window)
        self.sands_text.draw(self.window)
        self.zosin_text.draw(self.window)
        self.vinil_text.draw(self.window)
        self.ricardao_text.draw(self.window)

        self.exit_button.draw()

    def hide(self):
        self.is_open = False

        self.panel.undraw()
        self.title.undraw()

        self.tepe_text.undraw()
        self.leo_bom_text.undraw()
        self.mc_pose_text.undraw()
        self.sands_text.undraw()
        self.zosin_text.undraw()
        self.vinil_text.undraw()
        self.ricardao_text.undraw()

        self.exit_button.undraw()

    def update(self, mouse_position: Vector, mouse_click_position):
        self.exit_button.tick(mouse_position, mouse_click_position)
