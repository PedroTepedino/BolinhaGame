import random
from graphics import *


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

    fogo = Image(Point(150, 575), 'fogo.PNG')
    fogo2 = Image(Point(450, 575), 'fogo.PNG')
    fogo3 = Image(Point(750, 575), 'fogo.PNG')
    cloud = Image(Point(110, 25), 'cloud.JPG')
    cloud2 = Image(Point(310, 25), 'cloud.JPG')
    cloud3 = Image(Point(510, 25), 'cloud.JPG')
    cloud4 = Image(Point(700, 25), 'cloud.JPG')
    diabin = Image(Point(200, 555), 'diabin.PNG')
    diabin2 = Image(Point(600, 560), 'diabin.PNG')
    cloud.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    fogo.draw(window)
    fogo2.draw(window)
    fogo3.draw(window)
    diabin.draw(window)
    diabin2.draw(window)
    window.setBackground('gray')

# win = GraphWin("Bolinha Game", 800, 600)
# draw_ui(win)
# playing = True
#
# while playing:
#     key = win.checkKey()
#
#     if key == "Escape":
#         playing = False
#
# win.close()
