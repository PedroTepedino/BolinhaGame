import random

from graphics import *

win = GraphWin("Bolinha Game", 800, 600)
def draw_ui(window: GraphWin):
    linhaSuperior = Line(Point(0, 25), Point(800, 25))
    linhaSuperior.setWidth(50)
    linhaSuperior.setFill(color_rgb(50, 50, 180))
    linhaSuperior.draw(window)

    linhaInferior = Line(Point(0, 575), Point(800, 575))
    linhaInferior.setWidth(50)
    linhaInferior.setFill(color_rgb(250, 80, 80))
    linhaInferior.draw(window)

    linhaDireita = Line(Point(800, 50), Point(800, 550))
    linhaDireita.setWidth(25)
    linhaDireita.setFill(color_rgb(50, 50, 50))
    linhaDireita.draw(window)

    linhaEsquerda = Line(Point(0, 50), Point(0, 550))
    linhaEsquerda.setWidth(25)
    linhaEsquerda.setFill(color_rgb(50, 50, 50))
    linhaEsquerda.draw(window)

    
    win.setBackground('gray')

draw_ui(win)
playing = True

while playing:
    key = win.checkKey()

    if key == "Escape":
        playing = False

win.close()

