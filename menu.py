from graphics import *
import random

from scene import Scene
from button import Button
from vector import Vector

"""
O menu será inserido em uma janela de 800x600, possuindo assim, 
3 retangulos do meio pra baixo (play, credits, exit), um texto centralizado em cima, "Bolinha Game",
e uma bolinha no fundo indo e voltando batendo nas paredes.
"""


class Menu(Scene):

    def __init__(self, window: GraphWin, play_func, credits_func, exit_func):
        self.win = window

        self.mouse_position = Vector(0, 0)
        self.mouse_click = None

        self.title = Text(Point(400, 150), "Bolinha Game!")
        self.title.setSize(30)

        self.play_button = Button(window, play_func, Vector(400, 275), Vector(75, 25), "Play")
        self.credits_button = Button(window, credits_func, Vector(400, 350), Vector(75, 25), "Credits")
        self.exit_button = Button(window, exit_func, Vector(400, 425), Vector(75, 25), "Exit")

    def draw(self):
        self.title.draw(self.win)
        self.play_button.draw()
        self.credits_button.draw()
        self.exit_button.draw()


    def undraw(self):
        self.title.undraw()
        self.play_button.undraw()
        self.credits_button.undraw()
        self.exit_button.undraw()

    def tick(self):
        self.play_button.tick(self.mouse_position, self.mouse_click)
        self.credits_button.tick(self.mouse_position, self.mouse_click)
        self.exit_button.tick(self.mouse_position, self.mouse_click)

        # point = self.win.getMouse()
        # px, py = point.getX(), point.getY()
        #
        # x0, y0 = self.ret1.getP1().getX(), self.ret1.getP1().getY()
        # x1, y1 = self.ret1.getP2().getX(), self.ret1.getP2().getY()
        #
        # if ((min(x0, x1) <= px <= max(x0, x1)) and
        #         (min(y0, y1) <= py <= max(y0, y1))):
        #     print("Play")
        # else:
        #     print("Do nothing")
        #
        # x2, y2 = self.ret2.getP1().getX(), self.ret2.getP1().getY()
        # x3, y3 = self.ret2.getP2().getX(), self.ret2.getP2().getY()
        #
        # if ((min(x2, x3) <= px <= max(x2, x3)) and
        #         (min(y2, y3) <= py <= max(y2, y3))):
        #     print("Credits")
        # else:
        #     print("Do nothing")
        #
        # x4, y4 = self.ret3.getP1().getX(), self.ret3.getP1().getY()
        # x5, y5 = self.ret3.getP2().getX(), self.ret3.getP2().getY()
        #
        # if ((min(x4, x5) <= px <= max(x4, x5)) and
        #         (min(y4, y5) <= py <= max(y4, y5))):
        #     print("Exit")
        # else:
        #     print("Do nothing")




# class Menu(Scene):
#
#     def __init__(self, window: GraphWin):
#         self.win = window
#
#         self.ret1 = Rectangle(Point(300, 300), Point(500, 250))
#         self.t = Text(Point(400, 150), "Bolinha Game!")
#         self.play = Text(Point(400, 275), "Play")
#
#         self.ret2 = Rectangle(Point(300, 375), Point(500, 325))
#         self.credits = Text(Point(400, 350), "Credits")
#
#         self.ret3 = Rectangle(Point(300, 450), Point(500, 400))
#         self.exit = Text(Point(400, 425), "Exit")
#
#         self.draw()
#
#     def draw(self):
#
#         self.ret1.setOutline("black")
#         self.ret1.draw(self.win)
#
#         self.ret2.setOutline("black")
#         self.ret2.draw(self.win)
#
#         self.ret3.setOutline("black")
#         self.ret3.draw(self.win)
#
#         self.t.setOutline("black")
#         self.t.setSize(30)
#         self.t.draw(self.win)
#
#         self.play.setOutline("black")
#         self.play.setSize(20)
#         self.play.draw(self.win)
#
#         self.credits.setOutline("black")
#         self.credits.setSize(20)
#         self.credits.draw(self.win)
#
#         self.exit.setOutline("black")
#         self.exit.setSize(20)
#         self.exit.draw(self.win)
#
#     def undraw(self):
#         pass
#
#     def tick(self):
#         point = self.win.getMouse()
#         px, py = point.getX(), point.getY()
#
#         x0, y0 = self.ret1.getP1().getX(), self.ret1.getP1().getY()
#         x1, y1 = self.ret1.getP2().getX(), self.ret1.getP2().getY()
#
#         if ((min(x0, x1) <= px <= max(x0, x1)) and
#                 (min(y0, y1) <= py <= max(y0, y1))):
#             print("Play")
#         else:
#             print("Do nothing")
#
#         x2, y2 = self.ret2.getP1().getX(), self.ret2.getP1().getY()
#         x3, y3 = self.ret2.getP2().getX(), self.ret2.getP2().getY()
#
#         if ((min(x2, x3) <= px <= max(x2, x3)) and
#                 (min(y2, y3) <= py <= max(y2, y3))):
#             print("Credits")
#         else:
#             print("Do nothing")
#
#         x4, y4 = self.ret3.getP1().getX(), self.ret3.getP1().getY()
#         x5, y5 = self.ret3.getP2().getX(), self.ret3.getP2().getY()
#
#         if ((min(x4, x5) <= px <= max(x4, x5)) and
#                 (min(y4, y5) <= py <= max(y4, y5))):
#             print("Exit")
#         else:
#             print("Do nothing")


# win: para definir a janela
# rets: para os retangulos
# t: para o texto
# def menu():
#     win = GraphWin("MENU", 800, 600)
#
#     ret1 = Rectangle(Point(300, 300), Point(500, 250))
#     ret1.setOutline("black")
#     ret1.draw(win)
#
#     ret2 = Rectangle(Point(300, 375), Point(500, 325))
#     ret2.setOutline("black")
#     ret2.draw(win)
#
#     ret3 = Rectangle(Point(300, 450), Point(500, 400))
#     ret3.setOutline("black")
#     ret3.draw(win)
#
#     t = Text(Point(400, 150), "Bolinha Game!")
#     t.setOutline("black")
#     t.setSize(30)
#     t.draw(win)
#
#     play = Text(Point(400, 275), "Play")
#     play.setOutline("black")
#     play.setSize(20)
#     play.draw(win)
#
#     credits = Text(Point(400, 350), "Credits")
#     credits.setOutline("black")
#     credits.setSize(20)
#     credits.draw(win)
#
#     exit = Text(Point(400, 425), "Exit")
#     exit.setOutline("black")
#     exit.setSize(20)
#     exit.draw(win)
#
#     while True:
#         point = win.getMouse()
#         px, py = point.getX(), point.getY()
#
#         x0, y0 = ret1.getP1().getX(), ret1.getP1().getY()
#         x1, y1 = ret1.getP2().getX(), ret1.getP2().getY()
#
#         if ((min(x0, x1) <= px <= max(x0, x1)) and
#                 (min(y0, y1) <= py <= max(y0, y1))):
#             print("Play")
#         else:
#             print("Do nothing")
#
#         x2, y2 = ret2.getP1().getX(), ret2.getP1().getY()
#         x3, y3 = ret2.getP2().getX(), ret2.getP2().getY()
#
#         if ((min(x2, x3) <= px <= max(x2, x3)) and
#                 (min(y2, y3) <= py <= max(y2, y3))):
#             print("Credits")
#         else:
#             print("Do nothing")
#
#         x4, y4 = ret3.getP1().getX(), ret3.getP1().getY()
#         x5, y5 = ret3.getP2().getX(), ret3.getP2().getY()
#
#         if ((min(x4, x5) <= px <= max(x4, x5)) and
#                 (min(y4, y5) <= py <= max(y4, y5))):
#             print("Exit")
#         else:
#             print("Do nothing")
#
#     win.getMouse()
#     win.close()
#
#
# menu()
